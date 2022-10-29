from fastapi import APIRouter

oauthsRouter = APIRouter()


@oauthsRouter.route(path="/authorize", methods=["GET", "POST"])
def authorize():
    return {"StatusCode": 200}
