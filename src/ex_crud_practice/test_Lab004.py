# Fixture - a concept in python
#similar - pre condition - post condition

import pytest

@pytest.fixture
def Create_token():
    return "abc"

@pytest.fixture
def Create_booking_id():
    return 1

@pytest.fixture
def read_excel_file():
    return "xyz"

@pytest.fixture
def read_json_file():
    return {}

def test_consume(Create_token, Create_booking_id, read_excel_file,read_json_file):
    print(Create_token)
    print(Create_booking_id)
    print(read_excel_file)
    print(read_json_file)

def test_update_req_1(Create_token, Create_booking_id):
    print("create token ---->", Create_token)
    print("Booking id --->", Create_booking_id)


def test_update_req_2(Create_token, Create_booking_id):
    print("create token ---->", Create_token)
    print("Booking id --->", Create_booking_id)



