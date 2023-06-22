import logging
import traceback
from collections import Counter


class ProcessPage:
    @staticmethod
    def process_page(page_soup):
        element_text = []
        element_types = ["button", "nav", "a"]
        most_occur = ""
        i = 0

        for el in element_types:
            try:
                navs = page_soup.find_all(el)

                for nav in navs:
                    button_str = nav.text
                    new_str = button_str.strip()
                    if new_str != '':
                        element_text.append(new_str)
                    # print(nav.text)
                number_el = ProcessPage.count_elements(element_text)
                most_occur = number_el
            except Exception as e:
                print(traceback.format_exc())
                logging.error(traceback.format_exc())
            if most_occur != [] and most_occur != "undefined" and len(most_occur) > 0:
                return most_occur
            if len(most_occur) == 0:
                most_occur = ["No recognized elements"]
            if most_occur == ["null"]:
                most_occur = ["most_occur returned null"]
            print(el + " none on page")
            i = i + 1
            if i == len(element_types):
                return "No recognizable elements"

    @staticmethod
    def count_elements(el_array):
        counting = Counter(el_array)
        most_occur = counting.most_common(4)
        return most_occur