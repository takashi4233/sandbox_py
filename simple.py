import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://qiita.com/search/q=python/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    anchors = soup.find_all('searchResult_title')
    for anchor in anchors:
         print(anchor)


if __name__ == '__main__':
    main()
