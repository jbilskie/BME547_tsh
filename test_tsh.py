import pytest


@pytest.mark.parametrize("firstname, lastname, age, gender, tsh_data", [
                        ('John', 'Doe', 32, 'Male', [2.0, 1.4, 3.4, 3.3, 1.7]),
                        ('Amy', 'May', 3.5, 'Female', [1.001, 2.4445, 3.5]),
                        ('John', 'May', 89, 'male', [2.0, 1.4, 3.4, 3.3, 1.7]),
                        ('Amy', 'Doe', 28, 'Female', [1, 3.2, 3.0, 2.4, 3.5]),
                        ])
def test_create_patient(firstname, lastname, age, gender, tsh_data):
    from tsh_module import create_patient
    patient = create_patient(firstname, lastname, age, gender, tsh_data)
    fail = False
    if patient["First"] is not firstname:
        if patient["Last"] is not lastname:
            if patient["Age"] is not age:
                if patient["Gender"] is not gender.casefold():
                    if patient["TSH Data"] is not tsh_data:
                        fail = True

    assert fail is False


@pytest.mark.parametrize("firstname, lastname, age, gender, tsh_data, hypo", [
                        ('John', 'Doe', 32, 'Male', [2.0, 1.4, 3.3, 1], False),
                        ('Amy', 'May', 3.5, 'Female', [4.001, 2.45, 3], True),
                        ('John', 'May', 89, 'male', [2.0, 0.4, 3.4, 3], False),
                        ('Amy', 'Doe', 28, 'Female', [6, 3.2, 3, 3.5], True),
                        ])
def test_hypothyroidism(firstname, lastname, age, gender, tsh_data, hypo):
    from tsh_module import create_patient
    from tsh_module import declare_result
    patient = create_patient(firstname, lastname, age, gender, tsh_data)
    result = declare_result(patient)
    has_hypo = False
    if result == 'hypothyroidism':
        has_hypo = True

    assert has_hypo == hypo


@pytest.mark.parametrize("firstname, lastname, age, gender, tsh_data, hyper", [
                        ('John', 'Doe', 32, 'Male', [2.0, 1.4, 3.3, 1], False),
                        ('Amy', 'May', 3.5, 'Female', [0.99, 2.45, 3], True),
                        ('John', 'May', 89, 'male', [2.0, 0.4, 3.4, 3], True),
                        ('Amy', 'Doe', 28, 'Female', [6, 3.2, 3, 3.5], False),
                        ])
def test_hyperthyroidism(firstname, lastname, age, gender, tsh_data, hyper):
    from tsh_module import create_patient
    from tsh_module import declare_result
    patient = create_patient(firstname, lastname, age, gender, tsh_data)
    result = declare_result(patient)
    has_hyper = False
    if result == 'hyperthyroidism':
        has_hyper = True

    assert has_hyper == hyper
