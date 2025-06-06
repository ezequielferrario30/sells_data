from .country import Country
from .category import Category
from .city import City
from .customer import Customer
from .employee import Employee
from .product import Product
from .sale import Sale

class ModelFactory:
    """
    Factory Method para instanciar modelos de acuerdo a su tipo y datos de origen.
    """
    @staticmethod
    def create(model_type, data):
        """
        Crea una instancia del modelo correspondiente a partir de un dict o lista.

        :param model_type: str - nombre del modelo ('country', 'category', etc.)
        :param data: dict o lista - datos con los campos requeridos
        :return: Instancia de la clase modelo correspondiente
        """
        model_type = model_type.lower()
        if isinstance(data, dict):
            kwargs = data
        else:  # lista u otros
            raise ValueError("El parámetro 'data' debe ser un diccionario.")

        if model_type == 'country':
            return Country(kwargs['country_id'], kwargs['country_name'], kwargs['country_code'])
        elif model_type == 'category':
            return Category(kwargs['category_id'], kwargs['category_name'])
        elif model_type == 'city':
            return City(kwargs['city_id'], kwargs['city_name'], kwargs['zipcode'], kwargs['country_id'])
        elif model_type == 'customer':
            return Customer(kwargs['customer_id'], kwargs['first_name'], kwargs['middle_initial'],
                            kwargs['last_name'], kwargs['city_id'], kwargs['address'])
        elif model_type == 'employee':
            return Employee(kwargs['employee_id'], kwargs['first_name'], kwargs['middle_initial'],
                            kwargs['last_name'], kwargs['birth_date'], kwargs['gender'],
                            kwargs['city_id'], kwargs['hire_date'])
        elif model_type == 'product':
            return Product(kwargs['product_id'], kwargs['product_name'], kwargs['price'],
                           kwargs['category_id'], kwargs['product_class'], kwargs['modify_date'],
                           kwargs['resistant'], kwargs['is_allergic'], kwargs['vitality_days'])
        elif model_type == 'sale':
            return Sale(kwargs['sales_id'], kwargs['sales_person_id'], kwargs['customer_id'],
                        kwargs['product_id'], kwargs['quantity'], kwargs['discount'],
                        kwargs['total_price'], kwargs['sales_date'], kwargs['transaction_number'])
        else:
            raise ValueError(f"Modelo desconocido: {model_type}")
