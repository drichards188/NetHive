from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from processing.process_page import ProcessPage
from processing.process_selenium import process_selenium_page

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# need to switch to different target. tripadvisor is protected and obfuscates elements
# driver.get("https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS")
driver.get("https://www.finviz.com")
# more_buttons = driver.find_elements_by_class_name("moreLink")
# more_buttons = driver.find_elements(By.XPATH, '//button[normalize-space()="Read more"]')

# more_buttons = driver.find_elements(By.TAG_NAME, 'button')

# most of this section expands the comment buttons
try:
    table = driver.find_element(By.ID, "js-signals_1")

    more_buttons = driver.find_element(By.TAG_NAME, "div")
    my_span = driver.find_elements(By.XPATH, "//*[text()='Read more']")

    if my_span:
        for x in range(len(my_span)):
            # if my_span[x].is_displayed():
            driver.execute_script("arguments[0].click();", my_span[x])
            time.sleep(1)
        #     this gets the source code after comments are expanded
        page_source = driver.page_source
        process_page = process_selenium_page(page_source)
except Exception as e:
    if e == NoSuchElementException:
        print("no such element")
    print(f'error: {e}')


