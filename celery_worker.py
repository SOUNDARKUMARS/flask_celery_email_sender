from app import create_app, make_celery
import app.tasks # Import the tasks to ensure they are registered

# Initialize the Flask app and Celery
app = create_app()
celery = make_celery(app)

# Celery beat for schedule configuration for the daily newletter
celery.conf.beat_schedule={
    'send-hourly-newsletter':{
        'task':'app.tasks.hourly_news_letter',
        'schedule':120,
    }
}

if __name__ == '__main__':
    # Start the Celery worker and Beat scheduler
    celery.worker_main(argv=['worker', '--loglevel=info', '--beat'])
