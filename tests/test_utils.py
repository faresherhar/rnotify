from utils import generate_release_url


def test_generate_release_url_success():
    notification = generate_release_url(provider="github", repo_name="test_repo", tag_name="test_tag")
    assert isinstance(notification, str)


def test_generate_release_url_fail():
    notification = generate_release_url(provider="test_provider", repo_name="test_repo", tag_name="test_tag")
    assert notification == None
