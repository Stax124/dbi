import logging

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from ..database import create_session
from ..models import User
from ..shared import session_manager

router = APIRouter(tags=["users"])


@router.post("/create-user")
async def create_user(user: User):
    session = create_session()
    session.add(user)
    session.commit()
    return user


@router.get("/login")
async def login(email: str, password: str):
    logging.debug(f"Logging in user {email}")

    session = create_session()
    user = session.exec(
        select(User).where(User.email == email, User.password == password)
    ).first()

    if not user:
        return HTTPException(status_code=401, detail="User not found")

    token = session_manager.login(user)
    print("Token", token)
    return token


@router.post("/logout")
def logout(token: str):
    session_manager.logout(token)
    return {"message": "User logged out"}
