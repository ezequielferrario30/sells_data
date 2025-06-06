from src.models.sale import Sale

def test_sale_total():
    s = Sale(100, 1, 2, 3, 5, 0.10, 100.0, "2024-06-01", "X123")
    # total_price=100, discount=0.10, total=90
    assert s.total == 90.0

def test_sale_to_dict():
    s = Sale(101, 2, 3, 4, 2, 0.0, 50.0, "2024-06-01", "Y456")
    d = s.to_dict()
    assert d["sales_id"] == 101
    assert d["quantity"] == 2
    assert d["discount"] == 0.0
