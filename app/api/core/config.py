from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    AWS_COGNITO_POOL_ID: str
    AWS_COGNITO_CLIENT_ID: str
    AWS_COGNITO_REGION: str
    class Config:
        env_file = ".env"

settings = Settings()
