class Sale:
    def __init__(self, sales_id, sales_person_id, customer_id, product_id, quantity,
                 discount, total_price, sales_date, transaction_number):
        self._sales_id = sales_id
        self._sales_person_id = sales_person_id
        self._customer_id = customer_id
        self._product_id = product_id
        self._quantity = quantity
        self._discount = discount
        self._total_price = total_price
        self._sales_date = sales_date
        self._transaction_number = transaction_number

    @property
    def sales_id(self):
        return self._sales_id

    @property
    def total(self):
        """Devuelve el total después del descuento"""
        return self._total_price * (1 - self._discount)

    def __str__(self):
        return f"Sale({self.sales_id}): Product {self._product_id} x{self._quantity}, Total: {self._total_price}"

    def to_dict(self):
        return {
            "sales_id": self._sales_id,
            "sales_person_id": self._sales_person_id,
            "customer_id": self._customer_id,
            "product_id": self._product_id,
            "quantity": self._quantity,
            "discount": self._discount,
            "total_price": self._total_price,
            "sales_date": self._sales_date,
            "transaction_number": self._transaction_number
        }
