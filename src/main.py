import logging
import os
from logging import config as logging_config

from fastapi import Depends, FastAPI, HTTPException
from fastapi.logger import logger
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from src.routers.sales import router as sales_router
from src.routers.products import router as products_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=(
        "Accept",
        "Accept-Encoding",
        "Authorization",
        "Content-Type",
        "Origin",
        "User-Agent",
    ),
)


@app.on_event("startup")
async def startup() -> None:
    pass


@app.on_event("shutdown")
async def shutdown() -> None:
    pass


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


# users routes
app.include_router(sales_router, prefix="/sales", tags=["Sales"])
app.include_router(products_router, prefix="/products", tags=["Products"])

# our own custom logging config
logging_config.fileConfig(
    os.path.join(os.getcwd(), "src", "logging.conf"), disable_existing_loggers=False
)

# get the gunicorn logger so we can read in what log level the app is running with
app_logger = logging.getLogger("gunicorn.error")

# set the azure logger to warning so we don't get a ton of noise
azure_http_logger = logging.getLogger(
    "azure.core.pipeline.policies.http_logging_policy"
)
azure_http_logger.setLevel(logging.WARNING)

# set the fastapi logger to the same level as gunicorn
logger.handlers = app_logger.handlers
logger.setLevel(app_logger.level)
