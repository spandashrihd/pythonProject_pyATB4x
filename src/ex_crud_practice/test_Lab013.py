import pytest
import allure

@allure.title("TC#1 Verify that 2-2 is equal to 0")
@allure.description("This is a smoke TC, which checks - verify tat 2-2=0")
@pytest.mark.smoke
def test_sub1():
    assert 2-2==0

@allure.title("TC#2 Verify that 3-3 is equal to 0")
@allure.description("This is a smoke TC, which checks - verify tat 3-3=0")
@pytest.mark.regression
def test_sub2():
    assert 3-3==0

@allure.title("TC#3 Verify that 1-1 is equal to 0")
@allure.description("This is a smoke TC, which checks - verify tat 1-1=0")
@pytest.mark.smoke
def test_sub3():
    assert 1-1==0

@allure.title("TC#4 Verify that 0-0 is not equal to 0")
@allure.description("This is a smoke TC, which checks - verify tat 0-0!=0")
@pytest.mark.sanity
def test_sub4():
    assert 0-0!=0

@pytest.mark.skip(reason="Not working! Skip it.")
def test_sub5():
    assert 0-0!=0

