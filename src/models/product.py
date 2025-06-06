class Product:
    def __init__(self, product_id, product_name, price, category_id, product_class,
                 modify_date, resistant, is_allergic, vitality_days):
        self._product_id = product_id
        self._product_name = product_name
        self._price = price
        self._category_id = category_id
        self._product_class = product_class
        self._modify_date = modify_date
        self._resistant = resistant
        self._is_allergic = is_allergic
        self._vitality_days = vitality_days

    @property
    def product_id(self):
        return self._product_id

    @property
    def product_name(self):
        return self._product_name

    @property
    def price(self):
        return self._price

    def is_perishable(self):
        """Método de negocio: Determina si el producto es perecedero por los días de vitalidad"""
        return self._vitality_days > 0

    def __str__(self):
        return f"Product({self.product_id}): {self.product_name} (${self.price:.2f})"

    def to_dict(self):
        return {
            "product_id": self._product_id,
            "product_name": self._product_name,
            "price": self._price,
            "category_id": self._category_id,
            "product_class": self._product_class,
            "modify_date": self._modify_date,
            "resistant": self._resistant,
            "is_allergic": self._is_allergic,
            "vitality_days": self._vitality_days
        }
