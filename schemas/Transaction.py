from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from schemas.Base import Base
from schemas.mixins.int_id_pk import IntIdPkMixin


class Transaction(IntIdPkMixin, Base):
    __tablename__ = 'transaction'

    tariff: Mapped[str] = mapped_column()
