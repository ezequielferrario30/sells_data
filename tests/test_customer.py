from src.models.customer import Customer

def test_full_name():
    # Instanciamos (creamos un objeto) un cliente
    customer = Customer(1, "Eze", "E", "Ferrario", 4, "Av. Siempre Viva 123")
    
    # Chequeamos que la propiedad full_name funciona como esperamos
    assert customer.full_name == "Eze E. Ferrario"
    
    # Chequeamos que address guarda el valor correcto
    assert customer.address == "Av. Siempre Viva 123"

def test_to_dict():
    customer = Customer(2, "Ana", "", "Martínez", 7, "Calle Falsa 456")
    # El método to_dict() debería devolver un diccionario con los datos del cliente
    data = customer.to_dict()
    assert data["first_name"] == "Ana"
    assert data["last_name"] == "Martínez"
    assert data["city_id"] == 7
