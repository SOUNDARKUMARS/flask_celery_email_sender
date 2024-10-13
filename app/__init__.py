from flask import Flask
from celery import Celery
from app.config import Config
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

mail=Mail()
db=SQLAlchemy()

# Initialize Celery
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend='redis://localhost:6379/0',
        broker='redis://localhost:6379/0'
    )
    celery.conf.update(app.config)
    return celery

# Initialize Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # learn flask app.config later
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flask_email_sender.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    # Initialize Flaks-Mial
    mail.init_app(app)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
