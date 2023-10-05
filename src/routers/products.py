import logging

from fastapi import APIRouter, Depends, HTTPException
from src.dependancies.product_dependancy import get_product_repository
from src.repositories.product_repository import ProductRepository
from src.schemas import CategoryRequest, ProductRequest, InventoryRequest, InventoryEdit

router = APIRouter()


@router.post("/add-category")
async def add_category(
    product_repository: ProductRepository = Depends(get_product_repository),
    request: CategoryRequest = Depends(),
):
    """
    Add a category to the database

    Parameters:
        product_repository (ProductRepository): The product repository
        request (CategoryRequest): The category request schema

    Returns:
        dict: The category name
    """
    category = product_repository.create_category(request)
    logging.info(f"Created category {category.name} with id {category.id}")

    return {"category_name": category.name}


@router.get("/get-category/{category_id}")
async def get_category(
    category_id: int,
    product_repository: ProductRepository = Depends(get_product_repository),
):
    """
    Get a category from the database

    Parameters:
        category_id (int): The category id
        product_repository (ProductRepository): The product repository

    Returns:
        dict: The category
    """
    category = product_repository.get_category(category_id)
    if not category:
        raise HTTPException(status_code=500, detail="Category not found")
    return category


@router.get("/get-product/{product_id}")
async def get_product(
    product_id: int,
    product_repository: ProductRepository = Depends(get_product_repository),
):
    """
    Get a product from the database

    Parameters:
        product_id (int): The product id
        product_repository (ProductRepository): The product repository

    Returns:
        dict: The product
    """
    product = product_repository.get_product(product_id)
    if not product:
        raise HTTPException(status_code=500, detail="Product not found")
    return product


@router.post("/add-product")
async def add_product(
    product_repository: ProductRepository = Depends(get_product_repository),
    request: ProductRequest = Depends(),
):
    """
    Add a product to the database

    Parameters:
        product_repository (ProductRepository): The product repository
        request (ProductRequest): The product request schema

    Returns:
        dict: The product name
    """
    product = product_repository.create_product(request)
    logging.info(f"Created product {product.name} with id {product.id}")

    return {"product_name": product.name}


@router.post("/add-inventory")
async def add_inventory(
    product_repository: ProductRepository = Depends(get_product_repository),
    request: InventoryRequest = Depends(),
):
    """
    Add a inventory to the database

    Parameters:
        product_repository (ProductRepository): The product repository
        request (InventoryRequest): The inventory request schema

    Returns:
        dict: The inventory id
    """
    inventory = product_repository.create_product_inventory(request)
    logging.info(f"Created inventory for {inventory.product} with id {inventory.id}")

    return {
        "inventory_id": inventory.id,
    }


@router.patch("/update-inventory/{inventory_id}")
async def update_inventory(
    inventory_id: int,
    product_repository: ProductRepository = Depends(get_product_repository),
    request: InventoryEdit = Depends(),
):
    """
    Update a inventory in the database

    Parameters:
        inventory_id (int): The inventory id
        product_repository (ProductRepository): The product repository
        request (InventoryEdit): The inventory edit schema

    Returns:
        dict: The inventory id
    """
    inventory = product_repository.update_product_inventory(inventory_id, request)
    logging.info(f"Updated inventory for {inventory.product} with id {inventory.id}")

    return {
        "inventory_id": inventory.id,
    }


@router.get("/get-low-stock-inventory")
async def get_low_stock_inventory(
    product_repository: ProductRepository = Depends(get_product_repository),
):
    """
    Get low stock inventory from the database

    Parameters:
        product_repository (ProductRepository): The product repository

    Returns:
        dict: The inventory
    """
    low_stock_inventories = product_repository.get_low_stock_inventory()
    logging.info(f"Retrieved low stock inventory")

    return {
        "inventory": low_stock_inventories,
    }
