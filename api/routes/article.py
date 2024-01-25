import logging

from fastapi import APIRouter

from api.database import create_session
from api.models.article import Article

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/create-new-article")
async def create_new_article(article: Article):
    session = create_session()
