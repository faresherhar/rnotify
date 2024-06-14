from fastapi import APIRouter, status, Depends

from database import get_db_session
from cruds.repo import (
    get_repos,
    get_repos_by_provider,
    get_repos_by_owner,
    add_repo,
    delete_repo,
)


router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
async def get_repos_(db_session=Depends(get_db_session)):
    return get_repos(db_session=db_session)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_repo_(provider: str, owner: str, repo: str, db_session=Depends(get_db_session)):
    add_repo(provider=provider, owner=owner, repo=repo, db_session=db_session)
    return


@router.get("/{provider}", status_code=status.HTTP_200_OK)
async def get_repos_by_provider_(provider: str, db_session=Depends(get_db_session)):
    return get_repos_by_provider(provider=provider, db_session=db_session)


@router.get("/{provider}/{owner}", status_code=status.HTTP_200_OK)
async def get_repos_by_owner_(provider: str, owner: str, db_session=Depends(get_db_session)):
    return get_repos_by_owner(provider=provider, owner=owner, db_session=db_session)


@router.delete("/{provider}/{owner}/{repo}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_repo_(provider: str, owner: str, repo: str, db_session=Depends(get_db_session)):
    delete_repo(provider=provider, owner=owner, repo=repo, db_session=db_session)
    return
