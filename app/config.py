class Config:
    # Flask Configurations
    SECRET_KEY = 'your_secret_key'

    # Celery Configurations (new keys)
    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'

    # flask-mail configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'soundarkumarsaravanan@gmail.com'
    MAIL_PASSWORD = 'ecyg luxz nfte pmxl'
    MAIL_DEFAULT_SENDER = ('Flask Celery Mails', 'soundarkumarsaravanan@gmail.com')
