from jinja2 import Template
from json import loads

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import settings


def get_old_releases(db_seassion) -> set[tuple[str]]:
    releases = set()
    for key in db_seassion.keys():
        if key.startswith("celery-task-meta"):
            task = loads(db_seassion.get(key))
            if task["name"] == "rnotify.notifier.send_notification":
                releases.add(tuple(task["args"]))

    return releases


def generate_release_url(provider: str, repo_name: str, tag_name: str) -> str | None:
    if provider == "github":
        return f"https://github.com/{repo_name}/releases/tag/{tag_name}"
    elif provider == "gitlab":
        return f"https://gitlab.com/{repo_name}/-/releases/{tag_name}"


def render_notification_message(provider: str, repo_name: str, tag_name: str) -> str:
    with open(settings.notification_template) as file_:
        template = Template(file_.read())

        return template.render(
            provider=provider.title(),
            repo_name=repo_name,
            tag_name=tag_name,
            release_url=generate_release_url(
                provider=provider, repo_name=repo_name, tag_name=tag_name
            ),
        )


def send_email(
    subject: str,
    message_body: str,
    recipient: str,
    smtp_server: str,
    smtp_username: str,
    smtp_password: str,
    smtp_port: int = 465,
) -> None:

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = smtp_username
    message["To"] = recipient

    message.attach(MIMEText(message_body, "html"))
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient, message.as_string())
