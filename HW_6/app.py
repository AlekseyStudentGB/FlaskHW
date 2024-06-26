from fastapi import FastAPI
from db import db
from router import router
import uvicorn

app = FastAPI()


@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()


app.include_router(router, tags=['users'])

if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)