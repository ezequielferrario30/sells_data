class Country:
    def __init__(self, country_id, country_name, country_code):
        self._country_id = country_id
        self._country_name = country_name
        self._country_code = country_code

    @property
    def country_id(self):
        return self._country_id

    @property
    def country_name(self):
        return self._country_name

    @property
    def country_code(self):
        return self._country_code

    def __str__(self):
        return f"{self.country_name} ({self.country_code})"

    def to_dict(self):
        return {
            "country_id": self._country_id,
            "country_name": self._country_name,
            "country_code": self._country_code
        }
