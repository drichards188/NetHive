import logging
import traceback
from collections import Counter


class ProcessPage:
    @staticmethod
    def process_page(page_soup):
        element_text = []

        # there are no button elements, there are nav elements, and there are a elements
        # element_types = ["button", "nav", "a"]

        element_types = ["nav"]

        most_occur = ""
        i = 0

        for el in element_types:
            try:
                elements = page_soup.find_all(el)

                for nav in elements:
                    button_str = nav.text
                    new_str = button_str.strip()
                    no_newlines = new_str.replace("\n", "")

                    if no_newlines != '':
                        element_text.append(no_newlines)
                    # print(nav.text)
                number_el = ProcessPage.count_elements(element_text)
                most_occur = number_el
            except Exception as e:
                print(traceback.format_exc())
                logging.error(traceback.format_exc())
            if most_occur != [] and most_occur != "undefined" and len(most_occur) > 0:
                return most_occur
            else:
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