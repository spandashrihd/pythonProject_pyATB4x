#PUT requests
#URL
#path
#Token -Auth
#payload
#headers

import pytest
import requests
import allure

#create Token
def create_token():    #normal function, not a test
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    json_payload = {
    "username" : "admin",
    "password" : "password123"
    }

    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    #print(token)
    return token

#Create Booking
def Create_booking():
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
    print(booking_id)
    return booking_id

def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking/" + str(Create_booking())
    url = base_url + path_url
    cookie = "token=" + create_token()
    headers = {
        "Content-Type" : "application/json",
        "cookie" : cookie
         }
    json_payload= {
        "firstname": "Donald",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }
    response = requests.put(url=url, headers=headers, json=json_payload)

    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert response_data["firstname"] == "Donald"

#delete booking id
def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking"
    booking_id = Create_booking()
    Delete_url = URL + str(booking_id)
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie
    }

    response = requests.delete(url=Delete_url,headers=headers)
 