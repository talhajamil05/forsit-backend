# E-commerce Admin

# Requirements

1. Python 3.10.1

# Setup

1. Make sure python 3.10.1 is installed in the system either as default python version or through pyenv.
2. Navigate to root folder

3. Run the following commands to get started

```
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. alembic upgrade head
5. uvicorn sc.main:app --reload
```

The server will be up at http://127.0.0.1:8000

### API

1. The task is implemented using FAST API framework.
2. The base url is `http://127.0.0.1:8000`
3. API testing tools such as POSTMAN can be used to test the endpoints.

### Swagger UI to test endpoints

Api endpoints can be tested using swagger UI available at url is `http://127.0.0.1:8000/docs

### API ENDPOINTS

Api endpoints can be tested using swagger UI available at url is `http://127.0.0.1:8000/docs

1. **Sales Data**: `http://127.0.0.1:8000/sales/data`
   The endpoint accepts a GET request with the following optional query params as filters.

```
{
    "start_date": datetime,
    "end_date": datetime,
    "product_id": int,
    "category_id": int
}
```

2. **Get Revenue**: `http://127.0.0.1:8000/sales/get-revenue`
   The endpoint accepts a GET request with the following optional query params as filters.

```
{
    "start_date": datetime,
    "end_date": datetime,
    "category_id": int
}
```

3. **Add Product**: `http://127.0.0.1:8000/products/add-product`
   The endpoint accepts a POST request with the following request body and params as json.

```
{
    "name": str,
    "description": str,
    "price": int,
    "category_id": int
}
```

4. **Add Inventory**: `http://127.0.0.1:8000/products/add-inventory`
   the endpoint accepts a POST request with the following request body and params as json.

```
{
    "product_id": int,
    "current_stock": int
    "low_stock_alert_threshold": int
}
```

5. **Update Inventory**: `http://127.0.0.1:8000/products/update-inventory{inventory_id}`
   The endpoint accepts a PATCH request with the following request body and params as json.

```
{
    "inventory_id": int,
    "current_stock": int
    "low_stock_alert_threshold": int
}
```

6. **Low Stock Inventory**: `http://127.0.0.1:8000/products/get-low-stock-inventory`
   The endpoint accepts a GET request and returns low stock inventory from the database

### DATABASE MODELS

1. Category
2. Product (Each product will have a category)
3. Inventory (An inventory entry for each product)
4. Sale Items (Product items with a respective quatity to be associated with a sale entry)
5. Sales (Sales entry with multiple sale items)
