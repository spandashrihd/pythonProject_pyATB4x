import pytest
import allure
import requests

@allure.title("TC#1 - Create booking CRUD Positive")
@allure.description("TC#1 - Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # to make request
    # URL
    # Method: POST
    # Headers - Content-Type = Application/JSON
    # payload/data/body - dict/json
    # Auth(no)
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking"
    URL=base_url+path_url
    headers={"Content-Type" : "application/json"}
    payload={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
   }
    response=requests.post(url=URL, headers=headers, json=payload)

    #Response body verification
    #status code
    assert response.status_code == 200

    response_data=response.json()

    booking_id = response_data["bookingid"]
    assert booking_id is not None
    assert booking_id >0
    assert type(booking_id) == int

    firstname= response_data["booking"]["firstname"]
    lastname= response_data["booking"]["lastname"]
    totalprice = response_data["booking"]["totalprice"]
    depositpaid = response_data["booking"]["depositpaid"]
    checkin = response_data ["booking"]["bookingdates"]["checkin"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True
    assert checkin == "2018-01-01"


@allure.title("TC#2 - Create booking CRUD Negative")
@allure.description("TC#2 - Verify the create booking")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking"
    URL = base_url + path_url
    headers = {"Content-Type": "application/json"}
    json_payload = {}

    response=requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    #assertions
    assert response.status_code == 500

@allure.title("TC#3 - Create booking CRUD Negative")
@allure.description("TC#3 - Verify booking with totalprice is string negative")
@pytest.mark.crud
def test_create_booking_negative_tc3():   #Bug -- raise to client/developer
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking"
    URL = base_url + path_url
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : "python",
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
   }

    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Response body verification
    # status code
    assert response.status_code == 200










