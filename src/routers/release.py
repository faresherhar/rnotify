from fastapi import APIRouter, status, Depends

from database import get_db_session
from models.release import ReleaseSchema
from cruds.release import (
    get_all_releases,
    get_unnotified_releases,
    get_releases_by_provider,
    get_release
)


router = APIRouter()


@router.get("", response_model=list[ReleaseSchema], status_code=status.HTTP_200_OK)
async def  get_all_releases_(db_session=Depends(get_db_session)):
    return get_all_releases(db_session=db_session)


@router.get("/unnotified", response_model=list[ReleaseSchema], status_code=status.HTTP_200_OK)
async def  get_unnotified_releases_(db_session=Depends(get_db_session)):
    return get_unnotified_releases(db_session=db_session)


@router.get("/{provider}", response_model=list[ReleaseSchema], status_code=status.HTTP_200_OK)
async def get_releases_by_provider_(provider: str, db_session=Depends(get_db_session)):
    return get_releases_by_provider(provider=provider, db_session=db_session)


@router.get("/{provider}/{owner}/{repo}/{tag}", response_model=ReleaseSchema, status_code=status.HTTP_200_OK)
async def get_release_(provider: str, owner: str, repo: str, tag: str, db_session=Depends(get_db_session)):
    return get_release(provider=provider, owner=owner, repo=repo, tag=tag, db_session=db_session)
