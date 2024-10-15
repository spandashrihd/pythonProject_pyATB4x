import pytest
import requests


# Create token
@pytest.fixture
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    #print(token)
    return token


# Create booking
@pytest.fixture
def create_booking():
    print("Create booking testcase")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=url, headers=headers, json=json_payload)
    print(type(url))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


@pytest.fixture
def launch_browser():
    print("Launching browser")
    return "Chrome"


@pytest.fixture
def close_browser():
    print("Closing browser")
    return "closed"


@pytest.fixture
def read_url_testdata_excel():
    pass