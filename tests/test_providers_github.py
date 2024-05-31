from requests import Response

import providers.github


# Test successful calls
success_response = Response()
success_response.status_code = 200


def test_get_github_releases_success(mocker):
    mocker.patch("providers.github.get_github_releases", return_value=success_response)
    response = providers.github.get_github_releases(owner="owner", repo="repo")
    
    assert response.status_code == success_response.status_code


def test_get_github_latest_release_success(mocker):
    mocker.patch("providers.github.get_github_latest_release", return_value=success_response)
    response = providers.github.get_github_latest_release(owner="owner", repo="repo")
    
    assert response.status_code == success_response.status_code


def test_get_github_release_by_tag_name_success(mocker):
    mocker.patch("providers.github.get_github_release_by_tag_name", return_value=success_response)
    response = providers.github.get_github_release_by_tag_name(owner="owner", repo="repo", tag="tag")
    
    assert response.status_code == success_response.status_code


# Test failed calls
fail_response = Response()
fail_response.status_code = 404


def test_get_github_releases_fail(mocker):
    mocker.patch("providers.github.get_github_releases", return_value=fail_response)
    response = providers.github.get_github_releases(owner="owner", repo="repo")
    
    assert response.status_code == fail_response.status_code


def test_get_github_latest_release_fail(mocker):
    mocker.patch("providers.github.get_github_latest_release", return_value=fail_response)
    response = providers.github.get_github_latest_release(owner="owner", repo="repo")
    
    assert response.status_code == fail_response.status_code


def test_get_github_release_by_tag_name_fail(mocker):
    mocker.patch("providers.github.get_github_release_by_tag_name", return_value=fail_response)
    response = providers.github.get_github_release_by_tag_name(owner="owner", repo="repo", tag="tag")
    
    assert response.status_code == fail_response.status_code