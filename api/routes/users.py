import logging

from fastapi import APIRouter, HTTPException, Response
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


@router.get("/get-user")
async def get_user(token: str):
    user = session_manager.get_user(token)

    if user is None:
        return HTTPException(status_code=401, detail="User not found")

    return {
        "id": user.id,
        "username": user.username,
        "avatar": user.avatar,
    }


@router.get("/login")
async def login(email: str, password: str, response: Response):
    logging.debug(f"Logging in user {email}")

    session = create_session()
    user = session.exec(
        select(User).where(User.email == email, User.password == password)
    ).first()

    if not user:
        return HTTPException(status_code=401, detail="User not found")

    token = session_manager.login(user)
    print("Token", token)
    response.set_cookie(key="token", value=token)
    return {"token": token}


@router.post("/logout")
def logout(token: str):
    session_manager.logout(token)
    return {"message": "User logged out"}
