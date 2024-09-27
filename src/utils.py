import requests
from requests import Response
from urllib.parse import quote
from jinja2 import Template

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import settings
from models import Release


# Release
def gen_auth(api_token: str) -> dict[str]:
    "Generates an authentication dictionary."
    return {"Authorization": f"Bearer {api_token}"} if api_token != "" else {}


def get_github_latest_release(repo_name: str, api_token: str) -> Response:
    "Scrapess the latest github release for a specific github repository."
    return requests.get(
        settings.github_api_url + f"{repo_name}/releases/latest",
        headers=gen_auth(api_token=api_token),
    )


def get_gitlab_latest_release(repo_name: str, api_token: str) -> Response:
    "Scrapes the latest gitlab release for a specific gitlab repository."
    return requests.get(
        settings.gitlab_api_url
        + f"{quote(repo_name, safe='')}/releases/permalink/latest",
        headers=gen_auth(api_token=api_token),
    )


# Notification
def generate_release_url(provider: str, repo_name: str, tag_name: str) -> str:
    "Generates the URL for the release."
    if provider == "github":
        return f"https://github.com/{repo_name}/releases/tag/{tag_name}"
    elif provider == "gitlab":
        return f"https://gitlab.com/{repo_name}/-/releases/{tag_name}"


def render_notification_message(releases: set[Release]) -> str:
    "Generates the notification message, from a Jinja template."
    with open(settings.notification_template) as file_:
        template = Template(file_.read())

    return template.render(releases=releases)


# Email
def send_email(
    subject: str,
    message_body: str,
    recipient: str,
    smtp_server: str,
    smtp_username: str,
    smtp_password: str,
    smtp_port: int = 465,
) -> None:
    "Sends the nofication email."
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = smtp_username
    message["To"] = recipient

    message.attach(MIMEText(message_body, "html"))
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient, message.as_string())
