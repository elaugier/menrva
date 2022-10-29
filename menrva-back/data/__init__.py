from fastapi import APIRouter

dataRouter = APIRouter()


@dataRouter.get(path="/users")
async def get_users():
    return {"StatusCode": 200}
