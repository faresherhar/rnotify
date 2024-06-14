from fastapi import APIRouter, status, Depends

from database import get_db_session
from models.telegram import TelegramSchema
from models.slack import SlackSchema
from cruds.telegram import get_telegram_bots, add_telegram_bot, delete_telegram_bot
from cruds.slack import get_slack_webhooks, add_slack_webhook, delete_slack_webhook


router = APIRouter()


# Telegram
@router.get("/telegram", response_model=list[TelegramSchema], status_code=status.HTTP_200_OK)
async def  get_telegram_bots_(db_session=Depends(get_db_session)):
    return get_telegram_bots(db_session=db_session)


@router.put("/telegram", status_code=status.HTTP_200_OK)
async def  add_telegram_bot_(bot_token: str, chat_id: str, db_session=Depends(get_db_session)):
    return add_telegram_bot(bot_token=bot_token, chat_id=chat_id, db_session=db_session)


@router.delete("/telegram", status_code=status.HTTP_200_OK)
async def  delete_telegram_bot_(bot_token: str, chat_id: str, db_session=Depends(get_db_session)):
    return delete_telegram_bot(bot_token=bot_token, chat_id=chat_id, db_session=db_session)


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
