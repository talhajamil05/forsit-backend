from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.database import Base


class Sales(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )

    sale_items: Mapped["SaleItems"] = relationship(
        "SaleItems",
        uselist=True,
        back_populates="sales",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=functions.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=functions.now(),
        onupdate=functions.now(),
    )

    def get_total_price(self):
        total_price = 0
        for sale_item in self.sale_items:
            total_price += sale_item.get_total_price()
        return total_price
