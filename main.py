from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


from config.Database import db
from schemas.Base import Base
from routers.Presentation import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
