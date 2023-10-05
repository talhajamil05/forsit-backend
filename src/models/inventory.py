from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="inventory",
    )
    current_stock: Mapped[Integer] = mapped_column(Integer, nullable=False)
    low_stock_alert_threshold: Mapped[Integer] = mapped_column(
        Integer, nullable=False, default=1
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=functions.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=functions.now(),
        onupdate=functions.now(),
    )
