import json

import bs4
import requests
from urllib.parse import quote_plus

from fetcher.fetcher import Fetcher
from job_center.job_store import JobStore


class IndeedIngestor:
    def __init__(self, job_store: JobStore):
        self.base_url = 'https://www.indeed.com/jobs'
        self.job_store = job_store

    def construct_url(self, what, where, radius):
        """construct encoded url"""
        what = quote_plus(what)
        where = quote_plus(where)
        radius = quote_plus(radius)
        url = f'{self.base_url}?q={what}&l={where}&radius={radius}'
        return url

    def ingest(self, what: str, where: str, radius=25):
        """Ingest job information based on specified criteria.

           Args:
                what (str): Job descriptors, such as title, tools, programming languages, etc.
                where (str): Location of the job, e.g., "remote" or "San Francisco".
                radius (int, optional): Search radius for the location, in Miles. Default is 25.

           Returns:
                None

           This method constructs a URL by combining the provided job descriptors (what)
           and the job location (where), along with an optional search radius.
           The URL is used to fetch job information based on the specified criteria.
        """
        url = self.construct_url(what, where, radius)
        data = requests.get(url)
        return data


def main():
    # f = Fetcher()
    # url = "https://www.indeed.com/jobs?q=Data+scientist&l=Davis%2C+CA&radius=10"
    #
    # page = f.fetch_page(url)
    # print(page.contents)

    # page_source = open('sample-search-results.html').read()
    # page = bs4.BeautifulSoup(page_source, 'html.parser')
    #
    # mosaic_data = page.find('script', id='mosaic-data')
    # lines = mosaic_data.text.split('\n')
    # job_cards_line = [line for line in lines if 'mosaic-provider-jobcards' in line][0]
    # job_cards_json = '='.join(job_cards_line.split('=')[1:])[:-1]
    # open('job_cards.json', 'w').write(job_cards_json)

    job_cards = json.load(open('job_cards.json'))
    jobs = job_cards['metaData']['mosaicProviderJobCardsModel']['results']

    for i, j in enumerate(jobs):
        if j['expired']:
            continue

        link = j['viewJobLink'].split('&')[0]
        print(f"[{i}] title: {j['title']}, company: {j['company']}, link: https://www.indeed.com{link}")
    print('Done.')


if __name__ == '__main__':
    main()
