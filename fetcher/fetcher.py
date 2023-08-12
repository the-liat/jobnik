import json

import bs4
from selenium import webdriver


class Fetcher:
    def __init__(self):
        """ """
        self.driver = webdriver.Firefox()

    def _fetch_page_source(self, url):
        try:
            # Navigate to the URL
            self.driver.get(url)

            return self.driver.page_source
        finally:
            # Close the browser window
            self.driver.quit()

    def fetch_page(self, url):
        page_source = self._fetch_page_source(url)
        page = bs4.BeautifulSoup(page_source)
        return page


def main():
    f = Fetcher()
    url = "https://www.indeed.com/jobs?q=Data+scientist&l=Davis%2C+CA&radius=10"

    page = f.fetch_page(url)
    print(page.contents)

    # page_source = open('../job_ingestor/sample-search-results.html').read()
    # page = bs4.BeautifulSoup(page_source, 'html.parser')
    #
    # mosaic_data = page.find('script', id='mosaic-data')
    # lines = mosaic_data.text.split('\n')
    # job_cards_line = [line for line in lines if 'mosaic-provider-jobcards' in line][0]
    # job_cards_json = '='.join(job_cards_line.split('=')[1:])[:-1]
    # open('../job_ingestor/job_cards.json', 'w').write(job_cards_json)
    #
    # job_cards = json.load(open('../job_ingestor/job_cards.json'))
    # jobs = job_cards['metaData']['mosaicProviderJobCardsModel']['results']
    #
    # for i, j in enumerate(jobs):
    #     if j['expired']:
    #         continue
    #
    #     link = j['viewJobLink'].split('&')[0]
    #     print(f"[{i}] title: {j['title']}, company: {j['company']}, link: https://www.indeed.com{link}")
    print('Done.')


if __name__ == '__main__':
    main()
