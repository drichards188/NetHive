from bs4 import BeautifulSoup


def process_selenium_page(page_source):
    soup = BeautifulSoup(page_source, 'lxml')
    reviews = []
    reviews_selector = soup.find_all('div', class_='reviewSelector')
    for review_selector in reviews_selector:
        review_div = review_selector.find('div', class_='dyn_full_review')
        if review_div is None:
            review_div = review_selector.find('div', class_='basic_review')
        review = review_div.find('div', class_='entry').find('p').get_text()
        review = review.strip()
        reviews.append(review)
