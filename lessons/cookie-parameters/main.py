from typing import Annotated

from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/dashboard")
def get_cookie(
        username: Annotated[str | None, Cookie()] = None,
        *,
        theme: Annotated[str, Cookie()] = "light",
        language: Annotated[str, Cookie()] = "en",
        is_logged_in: Annotated[bool, Cookie(description="Use true or false.")] = False
):
    if not username:
        return {
            "message": "Welcome guest",
            "status": "Guest"
        }

    if is_logged_in:
        return {
            "message": f"Welcome {username}",
            "theme": theme,
            "language": language,
            "status": "logged in"
        }
    return {
        "message": f"Welcome {username}",
        "theme": theme,
        "language": language,
        "status": "Guest"
    }
