from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get("https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS")
# more_buttons = driver.find_elements_by_class_name("moreLink")
# more_buttons = driver.find_elements(By.XPATH, '//button[normalize-space()="Read more"]')

# more_buttons = driver.find_elements(By.TAG_NAME, 'button')

try:
    more_buttons = driver.find_element(By.TAG_NAME, "div")
    my_span = driver.find_elements(By.XPATH, "//*[text()='Read more']")
except Exception as e:
    if e == NoSuchElementException:
        print("no such element")
    print(f'error: {e}')

for x in range(len(my_span)):
    if my_span[x].is_displayed():
        driver.execute_script("arguments[0].click();", more_buttons[x])
        time.sleep(1)
page_source = driver.page_source
