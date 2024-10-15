from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from config.Database import db, secret_key
from routers.User import user_router
from schemas.Base import Base
from routers.Presentation import presentation_router
from sqladmin import Admin
from service.AdminAuth import AdminAuth
from views.UserAdmin import UserAdmin, ActionAdmin
from fastapi.middleware.cors import CORSMiddleware



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db.dispose()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
authentication_backend = AdminAuth(secret_key=secret_key)
admin = Admin(app, db.engine, authentication_backend=authentication_backend)

app.include_router(presentation_router)
app.include_router(user_router)
admin.add_view(UserAdmin)
admin.add_view(ActionAdmin)

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
