from turtle import title
from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from oauths import oauthsRouter
from data import dataRouter

title: str = "API de la Passion des Poèmes"
description: str = """
Bienvenue sur la documentation de l'API du site de la Passion des Poèmes. Cette dernière est en libre accès pour que vous puissiez
si le coeur vous en dit, développer votre propre site internet ou votre propre application. Seuls ne sont utilisables que les 
points d'entrée permettant de gérer les données d'un membre régulier ou privilège.
L'API concernant l'administration du site est réservé au webmaster et à son équipe de gestion.
"""
version: str = "1.0.0"

app = FastAPI(title=title, description=description, version=version)

app.include_router(router=oauthsRouter, prefix="/oauth", tags=["authentication"])
app.include_router(router=dataRouter, prefix="/data", tags=["data"])


@app.get("/", response_class=RedirectResponse)
def read_root():
    return "/docs"


@app.get("/pydantic", response_class=RedirectResponse, status_code=302)
async def redirect_pydantic():
    return "https://pydantic-docs.helpmanual.io/"
