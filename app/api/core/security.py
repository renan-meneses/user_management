import boto3
from fastapi import HTTPException, Depends
from app.core.config import settings

def cognito_authentication(token: str):
    client = boto3.client('cognito-idp', region_name=settings.AWS_COGNITO_REGION)
    
    try:
        response = client.get_user(
            AccessToken=token
        )
        return response
    except client.exceptions.NotAuthorizedException:
        raise HTTPException(status_code=401, detail="Unauthorized")

def get_current_user(token: str = Depends(cognito_authentication)):
    return token
