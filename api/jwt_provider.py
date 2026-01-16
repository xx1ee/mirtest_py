import jwt
from datetime import datetime, timezone, timedelta

class JWTProvider:
    SECRET = "test-secret"
    ALGORITHM = "HS256"

    @classmethod
    def generate(cls, user_id: int, role: str = "user") -> str:
        payload = {
            "sub": user_id,
            "role": role,
            "exp": datetime.now(timezone.utc) + timedelta(hours=1),
            "iat": datetime.now(timezone.utc)
        }

        return jwt.encode(payload, cls.SECRET, algorithm=cls.ALGORITHM)
