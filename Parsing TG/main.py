import requests
from bs4 import BeautifulSoup

k = 0

url = "https://tgstat.com/ru/ratings/channels?sort=members"

cookie = {
    'cf_clearance': '6YenUt_pzj120E72tLk0vj3QQjvNdLG3cR3N5tJrfws-1691757855-0-1-cffaf297.75aa331e.cac3e71-250.2.1691757855',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}

responce = requests.get(url, cookies=cookie, headers=header).text
soup = BeautifulSoup(responce, 'lxml')

block = soup.find('div', class_ = "sticky-center-column")
all_info = block.find_all('div', class_ = 'card peer-item-row mb-2 ribbon-box border')

for info in all_info:
    link_block = info.find('div', 'col col-12 col-sm-5 col-md-5 col-lg-4')
    tg_link = link_block.find('a').get('href')
    
    tg_link = str(tg_link)
    index = tg_link.find('channel/')
    tg_link = tg_link[index + 8:]
    tg_link = tg_link[:-5]
    
    info_storage = info.find('h4').text
    info_storage = info_storage.replace('\n', '').replace(' ', '')
    cnt = int(info_storage)
        
    if tg_link.count('@') == 0:
        tg_link = '@' + tg_link
    else:
        tg_link = tg_link

    file =  open('D:\\VSCode Projects\\Parsing\\Parsing TG\\TG Info', 'a')
    file.write(tg_link + '\n')
        
print('Данные добавлены в файл.')