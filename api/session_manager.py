import uuid
from typing import Dict, Optional

from api.models.user import User


class SessionManager:
    def __init__(self) -> None:
        self.sessions: Dict[str, User] = {}

    def login(self, user: User):
        assert user.id is not None

        token = uuid.uuid4().hex
        self.sessions[token] = user
        return token

    def logout(self, token: str):
        try:
            del self.sessions[token]
        except KeyError:
            pass

    def get_user(self, token: str) -> Optional[User]:
        try:
            return self.sessions[token]
        except KeyError:
            return None

    def is_logged_in(self, token: str) -> bool:
        return token in self.sessions
