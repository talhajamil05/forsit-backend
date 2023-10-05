import logging
from typing import Optional
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from src.dependancies.product_dependancy import get_product_repository
from src.repositories.product_repository import ProductRepository
from src.schemas import (
    CategoryRequest,
    ProductRequest,
    InventoryRequest,
    InventoryEdit,
    RevenueFilter,
)

router = APIRouter()


@router.get("/data")
async def get_sales_data(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    product_id: Optional[int] = None,
    category_id: Optional[int] = None,
    product_repository: ProductRepository = Depends(get_product_repository),
):
    """
    Get sales data from database

    Parameters:
        start_date (datetime): The start date
        end_date (datetime): The end date
        product_id (int): The product id
        category_id (int): The category id
        product_repository (ProductRepository): The product repository

    Returns:
        dict: The sales data
    """
    sales_data = product_repository.get_sales_data(
        start_date, end_date, product_id, category_id
    )
    data = []
    for sale in sales_data:
        data.append(
            {
                "sale_id": sale.id,
                "product_id": sale.product_id,
                "quantity": sale.quantity,
                "date": sale.created_at,
            }
        )
    return data


@router.get("/get-revenue")
async def get_revenue_from_sales(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    category_id: Optional[int] = None,
    product_repository: ProductRepository = Depends(get_product_repository),
):
    """
    Get sales revenue from database

    Parameters:
        start_date (datetime): The start date
        end_date (datetime): The end date
        category_id (int): The category id
        product_repository (ProductRepository): The product repository

    Returns:
        dict: The sales revenue
    """
    sales_data = product_repository.get_revenue_from_sales(
        start_date, end_date, category_id
    )

    return sales_data
