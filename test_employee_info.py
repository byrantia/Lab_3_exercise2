import employee_info

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(20,39)
    except_result = [ 
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert result == except_result



def test_calculate_average_salary():
    expected_result = 60166.67
    result = employee_info.calculate_average_salary()
    assert result == expected_result

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Marketing")
    expected_result = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]

    assert result == expected_result