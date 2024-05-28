from providers.github import (
    get_github_releases,
    get_github_latest_release,
    get_github_release_by_tag_name,
)


valid_test_data = {"owner": "grafana", "repo": "grafana", "tag": "v10.2.3"}
unvalid_test_data = {"owner": "unvalid_owner", "repo": "unvalid_repo", "tag": "unvalid_tag"}


# Test valid repo
def test_valid_get_github_releases():
    response = get_github_releases(owner=valid_test_data["owner"], repo=valid_test_data["repo"])
    assert response.status_code == 200


def test_valid_get_github_latest_release():
    response = get_github_latest_release(owner=valid_test_data["owner"], repo=valid_test_data["repo"])
    assert response.status_code == 200


def test_valid_get_github_release_by_tag_name():
    response = get_github_release_by_tag_name(owner=valid_test_data["owner"], repo=valid_test_data["repo"], tag=valid_test_data["tag"])
    assert response.status_code == 200


# Test unvalid repo
def test_unvalid_get_github_releases():
    response = get_github_releases(owner=unvalid_test_data["owner"], repo=unvalid_test_data["repo"])
    assert response.status_code == 404


def test_unvalid_get_github_latest_release():
    response = get_github_latest_release(owner=unvalid_test_data["owner"], repo=unvalid_test_data["repo"])
    assert response.status_code == 404


def test_unvalid_get_github_release_by_tag_name():
    response = get_github_release_by_tag_name(owner=unvalid_test_data["owner"], repo=unvalid_test_data["repo"], tag=unvalid_test_data["tag"])
    assert response.status_code == 404
