import logging

from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/alive")
async def test():
    return {"message": "Hello World"}
