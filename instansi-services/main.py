from fastapi import FastAPI
from instansis_route import router as instansis_router

app = FastAPI()

app.include_router(instansis_router)

@app.get("/")
async def read_main():
    return {"message": "Hello Bigger Applications!"}