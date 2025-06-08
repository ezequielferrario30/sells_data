from src.models.employee import Employee
from datetime import datetime

def test_employee_full_name():
    e = Employee(1, "Lucas", "J", "Fernandez", "1990-01-01", "M", 10, "2015-01-01 00:00:00")
    assert e.full_name == "Lucas J. Fernandez"

def test_employee_years_worked():
    e = Employee(2, "Sofia", "", "Lopez", "1985-06-06", "F", 3, "2020-01-01 00:00:00")
    current = datetime(2024, 6, 1)
    
    assert e.years_worked(current) in [4, 3]
