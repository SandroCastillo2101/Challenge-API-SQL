import requests

BASE_URL = "http://localhost:5000"


def test_get_employees_by_quarter():
    response = requests.get(f"{BASE_URL}/employees_by_quarter")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_hired_employees():
    response = requests.get(f"{BASE_URL}/hired_employees")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_upload_csv():
    response = requests.post(f"{BASE_URL}/upload_csv", "0")
    assert response.status_code == 400



