from ingestion.web_scrape import WebScrape


def main():
    target_url = "https://runescape.wiki/"

    scrape_results = WebScrape.get_page(target_url)
    print(scrape_results)

main()
