import pytest
import allure
import requests


@allure.title("Test GET request - RESTfull booker Project#1")
@allure.description("TC#1 - Verify that GET request to find ids of all the bookings")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Spanda")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_all_booking_id_positive_tc1():
    url="https://restful-booker.herokuapp.com/booking"
    response_data=requests.get(url)
    print(response_data)
    print(response_data.status_code)
    print(response_data.json())
    print(response_data.headers)
    print(response_data.text)
    assert response_data.status_code == 200

@allure.title("Test GET request - RESTfull booker Project#2")
@allure.description("TC#2 - Verify that GET request with invalid URL")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_all_booking_id_negative_tc2():
    url="https://restful-booker.herokuapp.com/booking123"
    response_data=requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET request - RESTfull booker Project#3")
@allure.description("TC#3 - Verify that GET request with invalid path param")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_all_booking_id_negative_tc3():
    url="https://restful-booker.herokuapp.com/booking/number/12"
    response_data=requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET request - RESTfull booker Project#4")
@allure.description("TC#4 - Verify that GET request with exceed ID limit")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_get_all_booking_id_negative_tc4():
    url="https://restful-booker.herokuapp.com/booking/2134567809876543"
    response_data=requests.get(url)
