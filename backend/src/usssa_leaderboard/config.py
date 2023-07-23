from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "USSSA Leaderboard"
    db_name: str = "leaderboard_db"
    mongodb_url: str = "mongodb://localhost:27017"

settings = Settings()
