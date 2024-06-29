from celery import Celery

from config import settings
from utils import send_email


app = Celery(
    "notifier",
    include=["tasks"],
    result_extended=True,
    broker=settings.broker_uri,
    backend=settings.backend_uri,
    broker_connection_retry_on_startup=True,
)


@app.task(name="rnotify.notifier.send_notification", max_retries=3)
def send_email_notification(message_body):
    send_email(
        "Rnotify Release Notification",
        message_body,
        settings.recipient,
        settings.smtp_server,
        settings.smtp_username,
        settings.smtp_password,
        settings.smtp_port,
    )

    return True


if __name__ == "__main__":
    worker = app.Worker(pool="solo", loglevel="INFO")
    worker.start()
