from fastapi import APIRouter

oauthsRouter = APIRouter()


@oauthsRouter.post(path="/authorize")
async def authorize():
    return {"StatusCode": 200}
