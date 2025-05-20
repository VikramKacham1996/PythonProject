import pytest
import allure
import requests


@allure.title("Verify GET request for booking ID 1")
@allure.description("This positive test case checks if booking ID 1 returns a successful response.")
@pytest.mark.positive
def test_get_request_pos():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    print(response_data.text)
    assert response_data.status_code == 200, "Expected status code 200, but got {response_data.status_code}"


@allure.title("Verify GET request for invalid booking ID (-1)")
@allure.description("This negative test case checks if an invalid booking ID returns a 404 Not Found.")
@pytest.mark.negative
def test_get_request_neg():
    url = "https://restful-booker.herokuapp.com/booking/-1"

    response_data = requests.get(url=url)
    print(response_data.text)
    assert response_data.status_code == 404, "Expected status code 404, but got {response_data.status_code}"




