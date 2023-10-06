from sqlalchemy import create_engine, text
import pandas as pd

SQLALCHEMY_DATABASE_URL = "mysql://root:    @localhost:3306/ecommerce_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
con = engine.connect()

category_insert_statement = text(
    """
INSERT INTO category (id, name, `desc`)
VALUES
  (1, 'cat1', 'test desc'),
  (2, 'cat2', 'test desc'),
  (3, 'cat3', 'test desc'),
  (4, 'cat4', 'test desc');
"""
)

con.execute(category_insert_statement)
con.commit()


product_insert_statement = text(
    """
INSERT INTO product (id, name, `desc`, category_id, price)
VALUES
  (1, 'prod1', 'test desc', 1, 10.0),
  (2, 'prod2', 'test desc', 2, 20.0),
  (3, 'prod3', 'test desc', 3, 30.0),
  (4, 'prod4', 'test desc', 4, 40.0);
"""
)
con.execute(product_insert_statement)
con.commit()


inventory_insert_statement = text(
    """
INSERT INTO inventory (id, product_id, current_stock, low_stock_alert_threshold)
VALUES
    (1, 1, 10, 1),
    (2, 2, 20, 2),
    (3, 3, 30, 3),
    (4, 4, 40, 4);
"""
)
con.execute(inventory_insert_statement)
con.commit()


sales_insert_statement = text(
    """
INSERT INTO sales (id)
VALUES
    (1),
    (2),
    (3),
    (4);
"""
)
con.execute(sales_insert_statement)
con.commit()


sale_items_insert_statement = text(
    """
INSERT INTO sale_items (id, sales_id, product_id, quantity)
VALUES
    (1, 1, 1, 3),
    (2, 1, 4, 1),
    (3, 2, 1, 3),
    (4, 2, 3, 6),
    (5, 2, 2, 5),
    (6, 2, 4, 2),
    (7, 3, 4, 6),
    (8, 3, 1, 2),
    (9, 3, 3, 5),
    (10, 4, 2, 4),
    (11, 4, 1, 3);
"""
)
con.execute(sale_items_insert_statement)
con.commit()

con.close()
