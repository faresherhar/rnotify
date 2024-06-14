from jinja2 import Environment, FileSystemLoader

from config import settings


# Notification message rendering
def generate_release_url(provider: str, owner: str, repo: str, tag: str) -> str | None:
    if provider == "github":
        return settings.GITHUB_RELEASE_URL.format(owner=owner, repo=repo, tag=tag)
    elif provider == "gitlab":
        return settings.GITLAB_RELEASE_URL.format(owner=owner, repo=repo, tag=tag)


def render_notification_message(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.txt.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag, release_url=generate_release_url(provider=provider, owner=owner, repo=repo, tag=tag))


def render_notification_message_markdown(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.md.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag, release_url=generate_release_url(provider=provider, owner=owner, repo=repo, tag=tag))
