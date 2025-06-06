from src.models.product import Product

def test_product_is_perishable():
    p = Product(1, "Manzana", 10.5, 2, "Fruta", "2024-06-01", "No", "No", 10)
    assert p.is_perishable() == True

    q = Product(2, "Lata de Atún", 15.0, 3, "Conserva", "2024-06-01", "Sí", "No", 0)
    assert q.is_perishable() == False

def test_product_str():
    p = Product(3, "Arroz", 20.0, 1, "Grano", "2024-06-01", "Sí", "No", 0)
    assert "Product(3): Arroz" in str(p)
