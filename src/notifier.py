from celery import Celery

from config import settings
from utils import render_notification_message, send_email


# Celery App configuration
app = Celery(
    "notifier",
    result_extended=True,
    broker=settings.broker_uri,
    backend=settings.backend_uri,
    broker_connection_retry_on_startup=True,
)


@app.task(name="rnotify.notifier.send_notification", max_retries=3)
def send_email_notification(provider: str, repo_name: str, tag_name: str):
    message_body = render_notification_message(provider=provider, repo_name=repo_name, tag_name=tag_name)    
    send_email(
        subject="Rnotify Release Notification",
        message_body=message_body,
        recipient=settings.recipient,
        smtp_server=settings.smtp_server,
        smtp_username=settings.smtp_username,
        smtp_password=settings.smtp_password,
        smtp_port=settings.smtp_port,
    )

    return True


if __name__ == "__main__":
    worker = app.Worker(pool="solo", loglevel="INFO")
    worker.start()
