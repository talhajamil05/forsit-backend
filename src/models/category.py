from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.database import Base


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    desc: Mapped[str | None] = mapped_column(String(200), nullable=True)
    product: Mapped["Product"] = relationship(
        "Product",
        uselist=True,
        back_populates="category",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=functions.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=functions.now(),
        onupdate=functions.now(),
    )
