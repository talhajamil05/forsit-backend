from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from src.models.category import Category
from src.models.product import Product


class CategoryRequest(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class ProductRequest(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

    class Config:
        orm_mode = True


class InventoryRequest(BaseModel):
    product_id: int
    current_stock: int
    low_stock_alert_threshold: int

    class Config:
        orm_mode = True


class InventoryEdit(BaseModel):
    current_stock: int
    low_stock_alert_threshold: int

    class Config:
        orm_mode = True


class RevenueFilter(BaseModel):
    start_date: Optional[int] = None
    end_date: Optional[int] = None
    category_id: Optional[int] = None

    class Config:
        orm_mode = True
