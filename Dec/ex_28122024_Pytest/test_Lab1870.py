import pytest
import allure

@allure.title("Verify that create booking with valid data")
@allure.description("This test case checks positive and negative test scenarios.")
@pytest.mark.positive
def test_create_booking_valid():
    print("Running valid booking test")
    assert 7 == 7

@allure.title("Verify that create booking with invalid data")
@allure.description("This test case checks negative test scenarios.")
@pytest.mark.negative
def test_create_booking_invalid():
    print("Running invalid booking test")
    assert 7 == 77



