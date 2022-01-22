import bs4
import requests
import logging
import collections

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'url',
    )
)


class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / '
                          '537.36(KHTML, likeGecko) Chrome / 97.0.4692.71Safari / 537.36'
        }

        self.result = []

    def load_page(self, page: int = None):
        url = 'https://www.avito.ru/ekaterinburg/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1&radius=200'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        self.parse_block(soup)
        return soup

    def parse_block(self, soup):
        logger.info(soup)
        logger.info('-' * 100)



    def run(self):
        text = self.load_page()
        self.parse_page(text=text)


if __name__ == '__main__':
    parser = Client()
    parser.run()
