import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://pycon.jp/2017/ja/sponsors/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='sponsor-content')
    for sponsor in sponsors:
        url = sponsor.h3.a['href']
        name = sponsor.h4.text
        print(name, url)


if __name__ == '__main__':
    main()
