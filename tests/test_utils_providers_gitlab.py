from src.utils.providers.gitlab import (
    get_gitlab_releases,
    get_gitlab_latest_release,
    get_gitlab_release_by_tag_name,
)


valid_repo = "AuroraOSS/AuroraStore"
valid_repo_tag_name = "3.2.8"

unvalid_repo = "sdfgdsfg/sdfgdsfgdsf"
unvalid_repo_tag_name = ""


# Test valid repo
def test_valid_gitlab_repo_releases():
    release = get_gitlab_releases(repo_name=valid_repo)
    assert isinstance(release, list)



def test_valid_gitlab_repo_latest_release():
    release = get_gitlab_latest_release(repo_name=valid_repo)
    assert isinstance(release, dict)


def test_valid_gitlab_repo_release_by_tag_name():
    release = get_gitlab_release_by_tag_name(
            repo_name=valid_repo, tag_name=valid_repo_tag_name
        )
    assert isinstance(release, dict)


# Test unvalid repo
def test_unvalid_gitlab_repo_releases():
    assert get_gitlab_releases(repo_name=unvalid_repo) is None


def test_unvalid_gitlab_repo_latest_release():
    assert get_gitlab_latest_release(repo_name=unvalid_repo) is None


def test_unvalid_gitlab_repo_release_by_tag_name():
    assert (
        get_gitlab_release_by_tag_name(
            repo_name=unvalid_repo, tag_name=valid_repo_tag_name
        )
        is None
    )
