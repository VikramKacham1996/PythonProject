import pytest
import allure
import requests


@allure.title("TC#1 -verify that 2-2=0")
@allure.description("This is basic math test")
@pytest.mark.smoke
def test_basic_math_1():
    assert 2-2 ==0


@allure.title("TC#2 -verify that 3-3=0")
@allure.description("This is basic math test")
@pytest.mark.regression
def test_basic_math_2():
    assert 3 - 3 == 0

@allure.title("TC#3 -verify that 3-3=0")
@allure.description("This is basic math test")
@pytest.mark.sanity
def test_basic_math_3():
    assert 1 - 1 == 0
