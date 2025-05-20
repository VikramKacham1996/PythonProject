# from  selenium import  webdriver
# import allure
# import pytest
# import time
#
#
# @allure.title("Open the app.vwo.com")
# @pytest.mark.regression
# def test_vwo_login():
#     driver = webdriver.Edge()
#     driver.get("https:/app.vwo.com")
#     time.sleep(15)



from selenium import webdriver
import allure
import pytest
import time

@allure.title("Open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(15)
    driver.quit()

