from src.utils.providers.github import (
    get_github_releases,
    get_github_latest_release,
    get_github_release_by_tag_name,
)


valid_repo = "grafana/grafana"
valid_repo_tag_name = "v10.2.3"

unvalid_repo = "sdfgdsfg/sdfgdsfgdsf"
unvalid_repo_tag_name = ""


# Test valid repo
def test_valid_github_repo_releases():
    release = get_github_releases(repo_name=valid_repo)
    assert isinstance(release, list)



def test_valid_github_repo_latest_release():
    release = get_github_latest_release(repo_name=valid_repo)
    assert isinstance(release, dict)


def test_valid_github_repo_release_by_tag_name():
    release = get_github_release_by_tag_name(
            repo_name=valid_repo, tag_name=valid_repo_tag_name
        )
    assert isinstance(release, dict)


# Test unvalid repo
def test_unvalid_github_repo_releases():
    assert get_github_releases(repo_name=unvalid_repo) is None


def test_unvalid_github_repo_latest_release():
    assert get_github_latest_release(repo_name=unvalid_repo) is None


def test_unvalid_github_repo_release_by_tag_name():
    assert (
        get_github_release_by_tag_name(
            repo_name=unvalid_repo, tag_name=valid_repo_tag_name
        )
        is None
    )
