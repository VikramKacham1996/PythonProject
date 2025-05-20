#Dynamically typed
# At the run time, data of the variable  can be changed. and you don't need to mention the data type -python -int is very smart

# AGE = 34
# age = 98
# print (age)
# print (AGE)
# print (type(age))
# print (type(AGE))
#
# age = "pramod"
# age = True
# print (type(age))


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")

# Give you time to log in manually
time.sleep(30)  # 🔁 You can increase this or replace it with login automation

# Wait for search bar to become visible
wait = WebDriverWait(driver, 30)
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Search')]")))

# Perform search
search_box.send_keys("QA Testing")
search_box.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()


