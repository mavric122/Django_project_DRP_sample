import requests
from bs4 import BeautifulSoup

url = 'https://getbootstrap.com/docs/5.2/content/typography/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
status_request = None


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def stasus_req():
    html = get_html(url)
    if html.status_code == 200:
        print('----------------------')
        print('Статус успешно получен')
        print('----------------------')
    else:
        print('----------------------')
        print('error')
        print('----------------------')
    return html.status_code


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# def parse(html):
#     if html.status_code == 200:
