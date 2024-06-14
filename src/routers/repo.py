from fastapi import APIRouter, status, Depends

from database import get_db_session
from models.repo import RepoSchema, ReposSchema
from cruds.repo import (
    get_repos,
    get_repos_by_provider,
    get_repos_by_owner,
    add_repo,
    delete_repo,
)


router = APIRouter()


@router.get("", response_model=list[RepoSchema], status_code=status.HTTP_200_OK)
async def get_repos_(db_session=Depends(get_db_session)):
    return get_repos(db_session=db_session)


@router.put("", status_code=status.HTTP_201_CREATED)
async def add_repo_(
    provider: str, owner: str, repo: str, db_session=Depends(get_db_session)
):
    return add_repo(provider=provider, owner=owner, repo=repo, db_session=db_session)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_repos(bulk_repos: ReposSchema, db_session=Depends(get_db_session)):
    for provider in bulk_repos.__dict__:
        for item in bulk_repos.__dict__[provider]:
            owner, repo = item.split("/")
            add_repo(provider=provider, owner=owner, repo=repo, db_session=db_session)

    return


@router.get(
    "/{provider}", response_model=list[RepoSchema], status_code=status.HTTP_200_OK
)
async def get_repos_by_provider_(provider: str, db_session=Depends(get_db_session)):
    return get_repos_by_provider(provider=provider, db_session=db_session)


@router.get(
    "/{provider}/{owner}",
    response_model=list[RepoSchema],
    status_code=status.HTTP_200_OK,
)
async def get_repos_by_owner_(
    provider: str, owner: str, db_session=Depends(get_db_session)
):
    return get_repos_by_owner(provider=provider, owner=owner, db_session=db_session)


@router.delete("/{provider}/{owner}/{repo}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_repo_(
    provider: str, owner: str, repo: str, db_session=Depends(get_db_session)
):
    return delete_repo(provider=provider, owner=owner, repo=repo, db_session=db_session)
