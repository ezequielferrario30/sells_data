class Employee:
    def __init__(self, employee_id, first_name, middle_initial, last_name, birth_date, gender, city_id, hire_date):
        self._employee_id = employee_id
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._birth_date = birth_date
        self._gender = gender
        self._city_id = city_id
        self._hire_date = hire_date

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def full_name(self):
        middle = f" {self._middle_initial}." if self._middle_initial else ""
        return f"{self._first_name}{middle} {self._last_name}"

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def hire_date(self):
        return self._hire_date

    def years_worked(self, current_date):
        """Devuelve los años trabajados (requiere datetime como current_date)"""
        from datetime import datetime
        try:
            hire = datetime.strptime(self._hire_date.split(" ")[0], "%Y-%m-%d")
            return (current_date - hire).days // 365
        except Exception:
            return None

    def __str__(self):
        return f"Employee({self.employee_id}): {self.full_name}, Hired: {self._hire_date}"

    def to_dict(self):
        return {
            "employee_id": self._employee_id,
            "first_name": self._first_name,
            "middle_initial": self._middle_initial,
            "last_name": self._last_name,
            "birth_date": self._birth_date,
            "gender": self._gender,
            "city_id": self._city_id,
            "hire_date": self._hire_date
        }
