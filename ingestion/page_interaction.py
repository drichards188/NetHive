from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get("https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS")
# more_buttons = driver.find_elements_by_class_name("moreLink")
# more_buttons = driver.find_elements(By.CLASS_NAME, '//TnInx')
# more_buttons = driver.find_elements(By.XPATH, '//button[normalize-space()="Read more"]')

more_buttons = driver.find_elements(By.TAG_NAME, 'button')

for x in range(len(more_buttons)):
    if more_buttons[x].is_displayed():
        driver.execute_script("arguments[0].click();", more_buttons[x])
        time.sleep(1)
page_source = driver.page_source
