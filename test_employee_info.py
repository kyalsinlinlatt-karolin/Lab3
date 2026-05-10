import employee_info

data = employee_info.employee_data

def test_get_employees_by_age_range():
    result = []
    expected_result = [data[1], data[2]]
    result = employee_info.get_employees_by_age_range(22, 30)
    assert(result == expected_result)   

def test_average_salary():
    expected_result = 60166.67
    result = employee_info.calculate_average_salary()
    assert(result == expected_result)

def test_get_employees_by_dept():
    expected_result = [data[0], data[5]]
    result = []
    result = employee_info.get_employees_by_dept("Sales")
    assert (result == expected_result)

