class Customer:
    def __init__(self, customer_id, first_name, middle_initial, last_name, city_id, address):
        self._customer_id = customer_id
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._city_id = city_id
        self._address = address

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def full_name(self):
        middle = f" {self._middle_initial}." if self._middle_initial else ""
        return f"{self._first_name}{middle} {self._last_name}"

    @property
    def city_id(self):
        return self._city_id

    @property
    def address(self):
        return self._address

    def __str__(self):
        return f"Customer({self.customer_id}): {self.full_name}, {self.address}"

    def to_dict(self):
        return {
            "customer_id": self._customer_id,
            "first_name": self._first_name,
            "middle_initial": self._middle_initial,
            "last_name": self._last_name,
            "city_id": self._city_id,
            "address": self._address
        }
