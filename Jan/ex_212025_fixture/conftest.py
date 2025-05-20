import pytest
import requests
from dotenv import load_dotenv
import os



@pytest.fixture()

def test_create_token():
    load_dotenv()
    username =os.getenv("USERNAME")
    password =os.getenv("PASSWORD")
    print(username,password)
    pass

@pytest.fixture()
def create_bookingid():
    print("Create Booking ID!!")
    URL = "https://restful-booker.herokuapp.com/booking"

@pytest.fixture
def read_mysql_file_database():
    pass
@pytest.fixture
def read_csv_file_database():
    pass
@pytest.fixture
def read_url_testdta_excel():
    pass

@pytest.fixture
def launch_browser():
    print("Launching a Browser!! Chrome")
    return "chrome"

@pytest.fixture
def close_browser():
    print("Closing a Browser!! Chrome")
    return "closed"


