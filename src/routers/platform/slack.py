from fastapi import APIRouter, status, Depends

from database import get_db_session
from models.platform.slack import SlackSchema
from cruds.platform.slack import get_slack_webhooks, add_slack_webhook, delete_slack_webhook


router = APIRouter()


# Slack
@router.get("/slack", response_model=list[SlackSchema], status_code=status.HTTP_200_OK)
async def  get_slack_webhooks_(db_session=Depends(get_db_session)):
    return get_slack_webhooks(db_session=db_session)


@router.put("/slack", status_code=status.HTTP_200_OK)
async def  add_slack_webhook_(webhook_token: str, db_session=Depends(get_db_session)):
    return add_slack_webhook(webhook_token=webhook_token, db_session=db_session)


@router.delete("/slack", status_code=status.HTTP_200_OK)
async def delete_slack_webhook_(webhook_token: str, db_session=Depends(get_db_session)):
    return delete_slack_webhook(webhook_token=webhook_token, db_session=db_session)
