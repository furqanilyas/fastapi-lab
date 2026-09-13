from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/verify")
def get_verify(
        *,
        user_agent: Annotated[str | None, Header()] = None,
        x_client_version: Annotated[str, Header()],
        x_token: Annotated[list[str], Header()]
):
    return {
        "User-Agent": user_agent,
        "X-Client-Version": x_client_version,
        "X-Token": x_token
    }


@app.get("/special")
def get_special(
        special_header: Annotated[str, Header(convert_underscores=False)]
):
    return special_header
