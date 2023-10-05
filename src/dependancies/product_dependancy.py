from fastapi import Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.repositories.product_repository import ProductRepository


def get_product_repository(db: Session = Depends(get_db)) -> ProductRepository:
    """
    Get user repository instance from database session for managing user data

    Parameters:
        db (Session): The database session

    Returns:
        UserRepository: The user repository instance
    """
    return ProductRepository(db)
