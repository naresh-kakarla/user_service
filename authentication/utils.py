import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings


class TokenManager:
    def __init__(self):
        jwt_config = settings.JWT_TOKEN
        self.secret_key = jwt_config["SECRET_KEY"]
        self.algorithm = jwt_config["ALG"]
        self.access_token_lifetime = jwt_config.get("ACCESS_TOKEN_LIFETIME", 15)
        self.refresh_token_lifetime = jwt_config.get("REFRESH_TOKEN_LIFETIME", 60)

    @property
    def access_token_expiry_seconds(self):
        return self.access_token_lifetime * 60

    @property
    def refresh_token_expiry_seconds(self):
        return self.refresh_token_lifetime * 60

    def generate_access_token(self, subject_id, is_client=False):
        now = datetime.now(timezone.utc)
        payload = {
            "sub": str(subject_id),
            "type": "client" if is_client else "user",
            "exp": now + timedelta(minutes=self.access_token_lifetime),
            "iat": now,
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def generate_refresh_token(self, username):
        now = datetime.now(timezone.utc)
        payload = {
            "sub": str(username),
            "type": "refresh",
            "exp": now + timedelta(minutes=self.refresh_token_lifetime),
            "iat": now,
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token):
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired."}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token."}
