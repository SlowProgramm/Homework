from fastapi import FastAPI
from view import router as view_router

app = FastAPI()
app.include_router(view_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# docker build . -t app