import json

import requests
from bs4 import BeautifulSoup

info_lst = []


def get_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / '
                      '537.36(KHTML, likeGecko) Chrome / 97.0.4692.71Safari / 537.36'
    }
    for page in range(1, 44):
        print(f'Парсинг {page} страницы...')
        url = 'https://shopping-mall.su/shops/krasota-i-zdorove/' + f'?PAGEN_1={page}'
        req = requests.get(url=url, headers=headers)
        req.encoding = 'utf-8'
        src = req.text

        soup = BeautifulSoup(src, 'lxml')

        block = soup.find_all(class_='shop-item')

        for item in block:
            title = item.find(class_='shop-item-header').find(class_='shop-item-name').text
            link = 'https://shopping-mall.su/' + item.find(class_='shop-item-header') \
                .find(class_='shop-item-name').get('href')
            text = item.find(class_='shop-item-detail-text-wrapper').text

            info_lst.append(
                {
                    'Title': title,
                    'link': link,
                    'text': text.strip(),
                }
            )



def dump_json(file_name):
    with open(f'{file_name}', 'w', encoding='utf-8') as file:
        json.dump(info_lst, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    dump_json('info.json')


if __name__ == '__main__':
    main()
