from fastapi import FastAPI
import logging

import logging_config
from routers import repo, release
from routers.platform import telegram, slack

# Define logger
logger = logging.getLogger(__name__)

# Define API
app = FastAPI()

# Connect routers
app.include_router(repo.router, prefix="/repos")
app.include_router(release.router, prefix="/releases")

app.include_router(telegram.router, prefix="/platforms")
app.include_router(slack.router, prefix="/platforms")
