from src.models.customer import Customer

def test_full_name():
    # creo el cliente
    customer = Customer(1, "Eze", "E", "Ferrario", 4, "Av. Siempre Viva 123")
    
    
    assert customer.full_name == "Eze E. Ferrario"
    
    assert customer.address == "Av. Siempre Viva 123"

def test_to_dict():
    customer = Customer(2, "Ana", "", "Martínez", 7, "Calle Falsa 456")
    # Si funciona, deja un diccionario con los datos del cliente 
    data = customer.to_dict()
    assert data["first_name"] == "Ana"
    assert data["last_name"] == "Martínez"
    assert data["city_id"] == 7
