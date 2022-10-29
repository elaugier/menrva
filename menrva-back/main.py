from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from oauths import oauthsRouter

app = FastAPI()


app.include_router(router=oauthsRouter, prefix="/oauth", tags=["authentication"])


@app.get("/", response_class=RedirectResponse)
def read_root():
    return "/docs"
