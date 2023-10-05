import logging
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from src.models.category import Category
from src.models.inventory import Inventory
from src.models.product import Product
from src.models.sale_items import SaleItems
from src.models.sales import Sales
from src.schemas import (
    CategoryRequest,
    InventoryRequest,
    ProductRequest,
    InventoryEdit,
    RevenueFilter,
)


class ProductRepository:
    """
    Repository for managing product and sales data
    """

    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category_create: CategoryRequest) -> Category:
        """
        Creates a category in SQL database and returns a Category object.

        Parameters:
            user_create (UserCreate): The user create schema

        Returns:
            Category: The category object
        """
        category = Category(
            name=category_create.name,
            desc=category_create.description,
        )
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def get_category(self, category_id: int) -> Optional[Category]:
        """
        Gets a category from SQL database and returns a Category object.

        Parameters:
            user_id (int): The user id

        Returns:
            Optional[Category]: The category object
        """
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_product(self, product_id: int) -> Optional[Product]:
        """
        Gets a product from SQL database and returns a Product object.

        Parameters:
            product_id (int): The product id

        Returns:
            Optional[Product]: The product object
        """

        return self.db.query(Product).filter(Product.id == product_id).first()

    def create_product(self, product_create: ProductRequest) -> Product:
        """
        Creates a product in SQL database and returns a Product object.

        Parameters:
            product_create (ProductCreate): The product create schema

        Returns:
            Product: The product object
        """
        product = Product(
            name=product_create.name,
            desc=product_create.description,
            price=product_create.price,
            category_id=product_create.category_id,
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all_products(self) -> Optional[list[Product]]:
        """
        Gets all products from SQL database and returns a list of Product objects.

        """
        return self.db.query(Product).all()

    def create_product_inventory(self, inventory_create: InventoryRequest) -> Inventory:
        """
        Creates a product inventory in SQL database and returns a Inventory object.

        Parameters:
            inventory_create (InventoryCreate): The inventory create schema

        Returns:
            Inventory: The inventory object
        """

        inventory = Inventory(
            product_id=inventory_create.product_id,
            current_stock=inventory_create.current_stock,
            low_stock_alert_threshold=inventory_create.low_stock_alert_threshold,
        )
        self.db.add(inventory)
        self.db.commit()
        self.db.refresh(inventory)
        return inventory

    def get_product_inventory(self, product_id: int) -> Optional[Inventory]:
        """
        Gets a product inventory from SQL database and returns a Inventory object.

        Parameters:
            product_id (int): The product id

        Returns:
            Inventory: The inventory object
        """
        return (
            self.db.query(Inventory).filter(Inventory.product_id == product_id).first()
        )

    def update_product_inventory(
        self, inventory_id: int, inventory_edit: InventoryEdit
    ) -> Optional[Inventory]:
        """
        Updates a product inventory in SQL database and returns a Inventory object.

        Parameters:
            inventory_id (int): The inventory id
            inventory_edit (InventoryEdit): The inventory edit schema

        Returns:
            Inventory: The inventory object
        """
        inventory = (
            self.db.query(Inventory).filter(Inventory.id == inventory_id).first()
        )
        inventory.current_stock = inventory_edit.current_stock
        inventory.low_stock_alert_threshold = inventory_edit.low_stock_alert_threshold
        inventory.updated_at = datetime.now()
        self.db.commit()
        self.db.refresh(inventory)
        return inventory

    def get_low_stock_products(self) -> Optional[list[Product]]:
        """
        Gets low stock products from SQL database and returns a list of Product objects.
        """
        return (
            self.db.query(Product)
            .join(Inventory)
            .filter(Inventory.current_stock <= Inventory.low_stock_alert_threshold)
            .all()
        )

    def get_low_stock_inventory(self) -> Optional[list[Inventory]]:
        """
        Gets low stock inventory from SQL database and returns a list of Inventory objects.

        Parameters:
            self (self): The class instance

        Returns:
            Optional[list[Inventory]]: The inventory object
        """
        return (
            self.db.query(Inventory)
            .filter(Inventory.current_stock <= Inventory.low_stock_alert_threshold)
            .all()
        )

    def get_sales_data(
        self,
        start_date: Optional[datetime],
        end_date: Optional[datetime],
        product_id: Optional[datetime],
        category_id: Optional[int],
    ):
        """
        Gets sales data from SQL database.

        Parameters:
            start_date (datetime): The start date
            end_date (datetime): The end date
            product_id (int): The product id
            category_id (int): The category id

        """

        return (
            self.db.query(Sales, SaleItems)
            .join(SaleItems)
            .join(Product)
            .filter(Sales.created_at >= start_date if start_date else True)
            .filter(Sales.created_at <= end_date if end_date else True)
            .filter(SaleItems.product_id == product_id if product_id else True)
            .filter(Product.category_id == category_id if category_id else True)
            .with_entities(
                Sales.id,
                SaleItems.product_id,
                Sales.created_at,
                SaleItems.quantity,
            )
            .all()
        )

    def get_revenue_from_sales(
        self,
        start_date: Optional[datetime],
        end_date: Optional[datetime],
        category_id: Optional[int],
    ):
        """
        Gets sales revenue from SQL database.

        Parameters:
            start_date (datetime): The start date
            end_date (datetime): The end date
            category_id (int): The category id

        """

        sales = (
            self.db.query(Sales)
            .join(SaleItems)
            .join(Product)
            .filter(Sales.created_at >= start_date if start_date else True)
            .filter(Sales.created_at <= end_date if end_date else True)
            .filter(Product.category_id == category_id if category_id else True)
            .with_entities(
                Sales,
            )
            .all()
        )
        sales_revenue = []
        for sale in sales:
            sales_revenue.append(
                {
                    "id": sale.id,
                    "total_price": sale.get_total_price(),
                    "created_at": sale.created_at,
                }
            )

        return sales_revenue
