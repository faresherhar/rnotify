from fastapi import FastAPI
import logging

import logging_config
from routers import repo, release
from routers.platform import telegram, slack

# Define logger
logger = logging.getLogger(__name__)

# Define API
app = FastAPI(
    title="Rnotify API",
    summary="A FastAPI for the Rnotify backend application.",
    description="Rnotify, is a Python tool for tracking releases. By using it, you are notified of the latest release of your configured repositories. It uses the Github, and Gitlab APIs to scrape the data of the releases related to your repositories, and sends you a message to notify you of the latest release, by Email, Slack, Telegram... .",
    version="1.0.0",
)

# Connect routers
app.include_router(repo.router, prefix="/repos")
app.include_router(release.router, prefix="/releases")

app.include_router(telegram.router, prefix="/platforms")
app.include_router(slack.router, prefix="/platforms")
