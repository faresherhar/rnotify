from requests import Response

from utils import generate_release_url, get_auth, send_email
import utils
from config import settings


# Test successful calls
success_response = Response()
success_response.status_code = 200

# Test failed calls
fail_response = Response()
fail_response.status_code = 404


# Generates authentication data
def test_get_auth_token():
    assert len(get_auth(api_token="API_TOKEN").keys()) == 1


def test_get_auth_empty():
    assert get_auth(api_token="") == {}


# Github calls
def test_get_github_latest_release_success(mocker):
    mocker.patch("utils.get_github_latest_release", return_value=success_response)
    response = utils.get_github_latest_release(owner="owner", repo="repo")

    assert response.status_code == success_response.status_code


def test_get_github_latest_release_fail(mocker):
    mocker.patch("utils.get_github_latest_release", return_value=fail_response)
    response = utils.get_github_latest_release(owner="owner", repo="repo")

    assert response.status_code == fail_response.status_code


# Gitlab calls
def test_get_gitlab_latest_release_success(mocker):
    mocker.patch("utils.get_gitlab_latest_release", return_value=success_response)
    response = utils.get_gitlab_latest_release(owner="owner", repo="repo")

    assert response.status_code == success_response.status_code


def test_get_gitlab_latest_release_fail(mocker):
    mocker.patch("utils.get_gitlab_latest_release", return_value=fail_response)
    response = utils.get_gitlab_latest_release(owner="owner", repo="repo")

    assert response.status_code == fail_response.status_code


# Release URL generation
def test_generate_release_url_success():
    notification = generate_release_url(provider="github", repo_name="test_repo", tag_name="test_tag")
    assert isinstance(notification, str)


def test_generate_release_url_fail():
    notification = generate_release_url(provider="test_provider", repo_name="test_repo", tag_name="test_tag")
    assert notification == None


# Send email
def test_send_email_success():
    send_email(
        subject="Test",
        message_body="Test Message",
        recipient=settings.recipient,
        smtp_server=settings.smtp_server,
        smtp_username=settings.smtp_username,
        smtp_password=settings.smtp_password,
        smtp_port=settings.smtp_port,
    )

    assert True


def test_send_email_fail():
    try:
        send_email(
            subject="Test",
            message_body="Test Message",
            recipient="recipient@example-email.com",
            smtp_server="smtp.example-email.com.com",
            smtp_username="username@example-email.com.com",
            smtp_password="password",
            smtp_port=465,
        )
    except:
        ...

    assert False
