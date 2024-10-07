from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column
from schemas.Base import Base
from schemas.mixins.int_id_pk import IntIdPkMixin


class Action(IntIdPkMixin, Base):
    __tablename__ = "action"

    senderId: Mapped[int] = mapped_column(ForeignKey("user.senderId"), nullable=False)

    actionStart: Mapped[int] = mapped_column(default=0)
    actionPayment: Mapped[int] = mapped_column(default=0)
    actionGeneration: Mapped[int] = mapped_column(default=0)
    actionLowGeneration: Mapped[int] = mapped_column(default=0)
    actionHighGeneration: Mapped[int] = mapped_column(default=0)
    actionSendUrl: Mapped[int] = mapped_column(default=0)
    actionSendPictures: Mapped[int] = mapped_column(default=0)
    actionSendDescription: Mapped[int] = mapped_column(default=0)
    actionSendType: Mapped[int] = mapped_column(default=0)
    actionCheckBalance: Mapped[int] = mapped_column(default=0)
    actionSuccessGeneration: Mapped[int] = mapped_column(default=0)
    actionSuccessPayment: Mapped[int] = mapped_column(default=0)
