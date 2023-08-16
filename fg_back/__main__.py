import os

import dotenv
import uvicorn
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(title="fg")


dotenv.load_dotenv()


DEBUG = str(os.getenv("DEBUG", False)).lower() in ("true", "1")


if DEBUG:

    @app.exception_handler(ValidationException)
    async def validation_exception_handler(
        request: Request, exc: ValidationException
    ):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": exc.errors()}),
        )


@app.get("/ping/")
def ping():
    return {"message": "pong"}


db_users = [
    {"id": 1, "email": "aaa@bbb.com"},
    {"id": 2, "email": "bbb@ccc.com"},
    {"id": 3, "email": "ccc@ddd.com"},
    {"id": 4, "email": "ddd@eee.com"},
]


@app.get("/api/users/")
def get_all_users():
    return db_users


@app.get("/api/users/{id}")
def get_user_by_id(id: int):
    for user in db_users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


class Tag(BaseModel):
    id: int
    name: str


class Item(BaseModel):
    id: int | None = None
    user_id: int
    name: str
    price_cents: int = Field(ge=0)
    tags: list[Tag] = Field(min_length=1)


db_items = [
    {
        "id": i,
        "name": f"item {i}",
        "user_id": 1,
        "price_cents": 1234,
        "tags": [{"id": 1, "name": "tag 1"}],
    }
    for i in range(1, 100)
]


@app.get(
    "/api/items/",
    response_model=list[Item],
)
def get_all_items(page: int = 1, limit: int = 6):
    # return db_items[(page - 1) * limit : (page) * limit]
    return db_items[(page - 1) * limit :][:limit]


@app.post("/api/items/many/")
def add_items(items: list[Item]):
    db_items.extend(items)
    return {"status": 200, "data": db_items}


if __name__ == "__main__":
    uvicorn.run(
        "fg_back.__main__:app",
        reload=True,
        host="0.0.0.0",
        port=5000,
        log_level="info",
    )
