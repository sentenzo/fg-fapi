import uvicorn
from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="fg")


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


db_items = [{"id": i, "name": f"item {i}"} for i in range(1, 100)]


@app.get("/api/items/")
def get_all_items(page: int = 1, limit: int = 6):
    # return db_items[(page - 1) * limit : (page) * limit]
    return db_items[(page - 1) * limit :][:limit]


if __name__ == "__main__":
    uvicorn.run(
        "fg_back.__main__:app",
        reload=True,
        host="0.0.0.0",
        port=5000,
        log_level="info",
    )
