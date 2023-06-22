import sys
import requests
import time
from bs4 import BeautifulSoup
from threading import Thread
import traceback
import logging

from processing.process_page import ProcessPage


# targetPage = event["webpage"]

class WebScrape:
    @staticmethod
    def get_page(target_page):
        page_soup = ""
        results = ""
        try:
            company_page = requests.get(target_page, timeout=5)

            if company_page:
                print("Visiting page ", target_page, )
                page_content = company_page.content
                page_soup = BeautifulSoup(page_content, "html.parser")

                results = ProcessPage.process_page(page_soup)
            else:
                print("Couldn't reach page")
                results = "Couldn't reach page"
                return results
        except Exception as e:
            print(traceback.format_exc())
            logging.error(traceback.format_exc())
        return results


