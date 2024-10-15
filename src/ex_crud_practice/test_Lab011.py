import pytest

import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Spanda")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

@pytest.mark.smoke
def test_verify_sum():
    assert 1+1==2

@pytest.mark.smoke
def test_verify_sum2():
    assert 1+1==5

@pytest.mark.reg
def test_verify_sum3():
    assert 40+10==50

def test_verify_sub():
    assert 7-1== 2

def test_verify_sub2():
    assert 70-20==50

@pytest.mark.skip("reason=Not Completed")
def test_verify_sub3():
    assert 50-10==20