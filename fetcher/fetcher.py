import bs4
from selenium import webdriver


class Fetcher:
    def __init__(self):
        """ """
        self.driver = webdriver.Chrome()

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


if __name__ == '__main__':
    main()
