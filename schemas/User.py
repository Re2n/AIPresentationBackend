from enum import unique

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from schemas.mixins.int_id_pk import IntIdPkMixin
from schemas.Base import Base
from schemas import Action


class User(IntIdPkMixin, Base):
    __tablename__ = "user"

    senderId: Mapped[int] = mapped_column(unique=True)
    nickname: Mapped[str] = mapped_column()
    username: Mapped[str]= mapped_column(nullable=True)
    balanceRub: Mapped[int] = mapped_column(default=0)
    balanceGeneration: Mapped[int] = mapped_column(default=0)