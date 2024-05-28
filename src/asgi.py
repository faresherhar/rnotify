from fastapi import FastAPI
import logging

import logging_config
from routers import release
from routers import repo


# Define logger
logger = logging.getLogger(__name__)

# Define API
app = FastAPI()

# Connect routers
app.include_router(release.router)
app.include_router(repo.router)
