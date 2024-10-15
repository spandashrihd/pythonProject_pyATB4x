#Create Booking TestCase
#Verify that Booking ID is not Null
#Status code, Headers.....
#Requests module - requests


import pytest            #pip install pytest
import allure            #pip install allure
import requests          #pip install requests
@allure.title("Test GET request - RESTfull booker Project#1")
@allure.description("TC#1 - Verify thatGET request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Spanda")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url)
    print(response_data)
    print(response_data.status_code)
    print(response_data.json())
    print(response_data.headers)
    print(response_data.text)
    assert response_data.status_code == 200

@allure.title("Test GET request - RESTfull booker Project#2")
@allure.description("TC#2 - Verify thatGET request with invalid ID")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url="https://restful-booker.herokuapp.com/booking/-1"
    response_data=requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET request - RESTfull booker Project#3")
@allure.description("TC#3 - Verify thatGET request with invalid ID")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url="https://restful-booker.herokuapp.com/booking/invalid"
    response_data=requests.get(url)
    assert response_data.status_code == 404