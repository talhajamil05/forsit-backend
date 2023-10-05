from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.database import Base
from src.models.inventory import Inventory
from src.models.sale_items import SaleItems

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    desc: Mapped[str | None] = mapped_column(String(200), nullable=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id"), nullable=False
    )
    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="product",
    )
    inventory: Mapped["Inventory"] = relationship(
        "Inventory",
        back_populates="product",
    )
    sale_items: Mapped["SaleItems"] = relationship(
        "SaleItems",
        uselist=True,
        back_populates="product",
    )
    price: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=functions.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=functions.now(),
        onupdate=functions.now(),
    )
