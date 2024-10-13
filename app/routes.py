from flask import Blueprint, jsonify,request
from app import db
from app.models import NewsLetterEmail

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask-Celery app!"})

@main.route('/start-task')
def start_task():
    # Delayed import to avoid circular import issues
    from app.tasks import long_task  
    task = long_task.delay()
    return jsonify({"task_id": task.id, "status": "Task started!"})

@main.route('/hourly-newsletter',methods=['POST'])
def hourly_newsletter():
    """Trigger hourly newsletter"""
    recipient=request.json.get('email')
    if recipient:
        existing_email=NewsLetterEmail.query.filter_by(email=recipient).first()
        if existing_email:
            return {"error":"This email is already registered"},409
        else:
            db.session.add(NewsLetterEmail(email=recipient))
            db.session.commit()
            return jsonify({"message":"Subscribed to newsletter","email":recipient}),201
    else:
        return jsonify({"error":"Email is required"})
    
@main.route('/unsubscribe',methods=["POST"])
def unsubscribe():
    email_to_unsub=request.json.get('email')
    if email_to_unsub:
        email_exist=NewsLetterEmail.query.filter_by(email=email_to_unsub).first()
        if email_exist:
            db.session.delete(email_exist)
            db.session.commit()
            return {"message":"Unsubscribed successfuly"},200
        else:
            return {"error":"You have not subscribed already"},409