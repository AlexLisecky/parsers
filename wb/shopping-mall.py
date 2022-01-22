import requests
from bs4 import BeautifulSoup
import json

url = 'https://shopping-mall.su/shops/dlya-doma-i-ofisa/'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / '
                  '537.36(KHTML, likeGecko) Chrome / 97.0.4692.71Safari / 537.36'
}

req = requests.get(url, headers=headers)
req.encoding = 'utf-8'
src = req.text

with open('index.html', 'w') as file:
    file.write(src)

with open('index.html') as file:
    src = file.read()

info_lst = []

soup = BeautifulSoup(src, 'lxml')
block = soup.find_all(class_='shop-right-block')
for item in block:
    name = item.find(class_='shop-item-name').text
    url = 'https://shopping-mall.su' + item.find(class_='shop-item-name').get('href')
    description = item.find(class_='shop-item-detail-text-wrapper').text
    description = description.replace('\n', '')
    info_lst.append(
        {
            'Name': name,
            'Url': url,
            'Description': description,
        }
    )

with open('info.json', 'w', encoding='utf-8') as file:
    json.dump(info_lst, file, indent=4, ensure_ascii=False)

with open('info.json', 'r', encoding='utf-8') as file:
    templates = json.load(file)




