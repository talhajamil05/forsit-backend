from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.database import Base
from src.models.sales import Sales

class SaleItems(Base):
    __tablename__ = "sale_items"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    product: Mapped["Product"] = relationship(
        "Product",
        uselist=True,
        back_populates="sale_items",
    )
    quantity: Mapped[Integer] = mapped_column(Integer, nullable=False, default=1)

    sales_id: Mapped[int] = mapped_column(ForeignKey("sales.id"), nullable=False)
    sales: Mapped["Sales"] = relationship(
        "Sales",
        back_populates="sale_items",
    )

    def get_total_price(self):
        return self.product_id.price * self.quantity
