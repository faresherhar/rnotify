from src.utils.renderer import render_notification


def test_text_notification():
    notification = render_notification(
        provider="test_provider",
        repo="test_repo",
        release_name="test_release_name",
        tag_name="test_tag_name",
        type="txt",
    )

    assert isinstance(notification, str)


def test_html_notification():
    notification = render_notification(
        provider="test_provider",
        repo="test_repo",
        release_name="test_release_name",
        tag_name="test_tag_name",
        type="html",
    )

    assert isinstance(notification, str)


def test_md_notification():
    notification = render_notification(
        provider="test_provider",
        repo="test_repo",
        release_name="test_release_name",
        tag_name="test_tag_name",
        type="md",
    )

    assert isinstance(notification, str)


def test_failed_notification():
    assert (
        render_notification(
            provider="test_provider",
            repo="test_repo",
            release_name="test_release_name",
            tag_name="test_tag_name",
            type="fail",
        )
        is None
    )
