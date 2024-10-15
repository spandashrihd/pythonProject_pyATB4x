import allure
import pytest
import requests

class Test_put_patch_request():
    def test_put_request(self, create_token, create_booking):
        base_url = "https://restful-booker.herokuapp.com"
        path_url = "/booking/" + str(create_booking)
        put_url = base_url + path_url
        cookie = "token=" + create_token
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }
        json_payload = {
            "firstname": "Spanda",
            "lastname": "Gowda",
            "totalprice": 500,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = requests.put(url=put_url, headers=headers, json=json_payload)
        assert response.status_code == 200
        data = response.json()
        print(data)

        assert data['firstname'] == "Spanda"
        assert data['lastname'] == "Gowda"
        assert data['depositpaid'] == True

    def test_patch_request(self, create_token, create_booking):
        base_url = "https://restful-booker.herokuapp.com"
        path_url = "/booking/" + str(create_booking)
        put_url = base_url + path_url
        cookie = "token=" + create_token
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }
        json_payload = {
            "firstname": "Deepa",
            "lastname": "Shetty"
        }
        response = requests.patch(url=put_url, headers=headers, json=json_payload)
        assert response.status_code == 200
        data = response.json()
        print(data)

        assert data['firstname'] == "Deepa"
        assert data['lastname'] == "Shetty"
