class City:
    def __init__(self, city_id, city_name, zipcode, country_id):
        self._city_id = city_id
        self._city_name = city_name
        self._zipcode = zipcode
        self._country_id = country_id

    @property
    def city_id(self):
        return self._city_id

    @property
    def city_name(self):
        return self._city_name

    @property
    def zipcode(self):
        return self._zipcode

    @property
    def country_id(self):
        return self._country_id

    def __str__(self):
        return f"{self.city_name} ({self.zipcode})"

    def to_dict(self):
        return {
            "city_id": self._city_id,
            "city_name": self._city_name,
            "zipcode": self._zipcode,
            "country_id": self._country_id
        }
