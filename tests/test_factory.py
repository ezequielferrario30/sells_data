from src.models.factory import ModelFactory

def test_factory_customer():
    data = {
        "customer_id": 1,
        "first_name": "Pepe",
        "middle_initial": "",
        "last_name": "Argento",
        "city_id": 99,
        "address": "Tv. del Bueno 456"
    }
    customer = ModelFactory.create("customer", data)
    assert customer.full_name == "Pepe Argento"

def test_factory_sale():
    data = {
        "sales_id": 1,
        "sales_person_id": 2,
        "customer_id": 3,
        "product_id": 4,
        "quantity": 5,
        "discount": 0.2,
        "total_price": 100.0,
        "sales_date": "2024-06-01",
        "transaction_number": "Z123"
    }
    sale = ModelFactory.create("sale", data)
    assert sale.total == 80.0
