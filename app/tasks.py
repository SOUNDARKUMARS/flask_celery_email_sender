from app import create_app, make_celery, mail, db
from app.models import NewsLetterEmail
from flask_mail import Message

app = create_app()
celery = make_celery(app)

@celery.task(name='app.tasks.hourly_news_letter')
def hourly_news_letter():
    """Task to send hourly newsletters to all emails in the database."""
    subject = "Your Hourly Newsletter"
    body = "This is your hourly newsletter."

    # Use the Flask application context to access the database
    with app.app_context():
        emails = NewsLetterEmail.query.all()

        if not emails:
            print("No emails to send.")
            return "No emails to send."

        for email in emails:
            send_email_task(subject, email.email, body)  # Send email to each recipient

    return "Emails sent."

@celery.task(name='app.tasks.send_email_task')
def send_email_task(subject, recipient, body):
    """Task to send an email."""
    with app.app_context():
        msg = Message(subject, recipients=[recipient], body=body)
        mail.send(msg)
        print(f"Email sent to {recipient}")
    return f"Email sent to {recipient}"
