from utils import render_notification, render_notification_markdown


def test_render_notification():
    notification = render_notification(
        provider="test_provider",
        owner="test_owner",
        repo="test_repo",
        tag="test_tag",
    )

    assert isinstance(notification, str)


def test_render_notification_markdown():
    notification = render_notification_markdown(
        provider="test_provider",
        owner="test_owner",
        repo="test_repo",
        tag="test_tag",
    )

    assert isinstance(notification, str)
