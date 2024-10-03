from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from schemas.mixins.int_id_pk import IntIdPkMixin
from schemas.Base import Base


class Presentation(IntIdPkMixin, Base):
    __tablename__ = 'presentation'

    name: Mapped[str] = mapped_column()
