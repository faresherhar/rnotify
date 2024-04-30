from jinja2 import Environment, FileSystemLoader
import logging

import utils.logging_config
from config import settings


# Define logger
logger = logging.getLogger(__name__)


SUPPORTED_TYPES = ["html", "txt", "md"]
is_suppotred_type = lambda x: x in SUPPORTED_TYPES


def generate_release_url(provider: str, repo: str, tag_name: str) -> str | None:
    if provider == "github":
        return settings.GITHUB_RELEASE.format(repo=repo, tag_name=tag_name)
    if provider == "gitlab":
        return settings.GITLAB_RELEASE.format(repo=repo, tag_name=tag_name)


def render_notification(
    provider: str, repo: str, tag_name: str, type: str = "txt"
) -> str | None:
    if not is_suppotred_type(type):
        logger.warning(f"Message type {type} not found")
        return None

    environment = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES))
    template = environment.get_template(f"notification.{type}")

    return template.render(
        provider=provider.title(),
        repo=repo,
        tag_name=tag_name,
        release_url=generate_release_url(
            provider=provider, repo=repo, tag_name=tag_name
        ),
    )
