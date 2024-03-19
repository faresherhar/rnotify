from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pytest
import json
import os

from cruds.repo import add_release, get_all_releases, get_releases, get_release
from models.repo import Repo


# Test DB
TEST_DB = "test.db"

# Create DB
engine = create_engine(f"sqlite:///{TEST_DB}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create table
Repo.metadata.create_all(bind=engine)


@pytest.fixture(autouse=True)
def run_rm_test_db():
    assert True
    yield
    os.remove(TEST_DB)
    assert True


# add_release
def test_add_release_github():
    try:
        with open("samples/release/github_release_body.json") as file:
            release_body = json.load(file)
            add_release(
                provider="github",
                repo_name="grafana/grafana",
                tag_name=release_body["tag_name"],
                release_body=release_body,
                db_session=SessionLocal(),
            )
        assert True
    except SQLAlchemyError:
        assert False


def test_add_release_exists_github():
    test_add_release_github()


def test_add_release_gitlab():
    try:
        with open("samples/release/gitlab_release_body.json") as file:
            release_body = json.load(file)
            add_release(
                provider="gitlab",
                repo_name="AuroraOSS/AuroraStore",
                tag_name=release_body["tag_name"],
                release_body=release_body,
                db_session=SessionLocal(),
            )
        assert True
    except SQLAlchemyError:
        assert False


def test_add_release_exists_gitlab():
    test_add_release_gitlab()


# get_all_releases
def test_get_all_releases():
    assert get_all_releases(db_session=SessionLocal()) != []


# get_releases
def test_get_github_releases():
    assert get_releases(provider="github", db_session=SessionLocal()) != []


def test_get_gitlab_releases():
    assert get_releases(provider="gitlab", db_session=SessionLocal()) != []


def test_get_unkown_provider_releases():
    assert get_releases(provider="unkown_provider", db_session=SessionLocal()) == []


# get_release
def test_get_exists_release():
    release = get_release(
        provider="github",
        repo_name="grafana/grafana",
        tag_name="v10.2.3",
        db_session=SessionLocal(),
    )

    assert isinstance(release, Repo)


def test_get_no_exists_release():
    assert (
        get_release(
            provider="gitlab",
            repo_name="AuroraOSS/AuroraStore",
            tag_name="v2.3.4",
            db_session=SessionLocal(),
        )
        is None
    )
