import pytest
import allure
import requests

#pip install pytest allure requests

@allure. title ("Tc#1- create booking crud positive")
@allure.description ("verify the create booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url="https://resrful-booker.herokuapp.com"
    base_path_post="/booking"

    full_url = base_url+base_path_post
    headers = {
    }

    pass


@allure. title ("Tc#2 - create booking crud negative")
@allure.description ("verify that invalid payload booking is not created")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    pass
