from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import random
import string
import time
import os

browser_choice = "chrome"
def random_word(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
def random_number(length):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))
def create_driver(browser_choice):
    if browser_choice.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser_choice.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    elif browser_choice.lower() == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_choice}")
    return driver

driver = create_driver(browser_choice)
wait = WebDriverWait(driver, 15)
try:
    driver.get("https://pwiddy.interview.tisostudio.com/")
    search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search for restaurants...']")))
    search_input.send_keys("West, Mayer and Wintheiser")
    time.sleep(2)
    search_input.send_keys(Keys.ENTER)

    restaurant = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/a[1]/div[2]")))
    restaurant.click()
    time.sleep(3)
    add_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(text(),'Add')]")))
    for i in range(min(3, len(add_buttons))):
        add_buttons[i].click()
        time.sleep(1)

    cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='relative']")))
    cart_button.click()
    checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Proceed to Checkout']")))
    checkout_button.click()
    time.sleep(2)
    street_name = ["Street", "Avenue", "Boulevard", "Lane", "Road"]
    random_address = random_word(8) + " " + random.choice(street_name)
    random_city = random_word(6)
    random_zip = random_number(6)
    random_phone = random_number(10)

    address_input = wait.until(EC.visibility_of_element_located((By.NAME, "address")))
    address_input.send_keys(random_address)

    city = wait.until(EC.visibility_of_element_located((By.NAME, "city")))
    city.send_keys(random_city)

    zip_code = wait.until(EC.visibility_of_element_located((By.ID, "zipCode")))
    zip_code.send_keys(random_zip)

    phone_no = wait.until(EC.visibility_of_element_located((By.ID, "phone")))
    phone_no.send_keys(random_phone)
    print(f"Order Details:\nAddress: {random_address}\nCity: {random_city}\nZip Code: {random_zip}\nPhone No: {random_phone}")
    time.sleep(2)

    place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Place Order']")))
    place_order_button.click()

    confirmation = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[1]/h1')))
    print(" Order placed successfully on", browser_choice)
except Exception as e:
    print(" Test failed:", e)

finally:
    time.sleep(5)
    driver.quit()