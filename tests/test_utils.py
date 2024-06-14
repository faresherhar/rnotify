from utils import render_notification_message, render_notification_message_markdown, generate_release_url


def test_generate_release_url_success():
    notification = generate_release_url(provider="github", owner="test_owner", repo="test_repo", tag="test_tag")
    assert isinstance(notification, str)


def test_generate_release_url_fail():
    notification = generate_release_url(provider="test_provider", owner="test_owner", repo="test_repo", tag="test_tag")
    assert notification == None


def test_render_notification_message():
    notification = render_notification_message(provider="test_provider", owner="test_owner", repo="test_repo", tag="test_tag")
    assert isinstance(notification, str)


def test_render_notification_message_markdown():
    notification = render_notification_message_markdown(provider="test_provider", owner="test_owner", repo="test_repo", tag="test_tag")
    assert isinstance(notification, str)
