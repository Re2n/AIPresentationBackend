from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


from config.Database import db
from routers.User import user_router
from schemas.Action import Action
from schemas.Base import Base
from routers.Presentation import presentation_router
from sqladmin import Admin, ModelView

from views.UserAdmin import UserAdmin, ActionAdmin


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db.dispose()


app = FastAPI(lifespan=lifespan)
admin = Admin(app, db.engine)

#app.include_router(presentation_router)
app.include_router(user_router)
admin.add_view(UserAdmin)
admin.add_view(ActionAdmin)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
