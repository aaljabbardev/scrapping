import requests
from bs4 import BeautifulSoup

try:
    url = 'https://detik.com'
    r = requests.get(url)
    # print(r.text)
    soup = BeautifulSoup(r.text, features="html.parser")
    print(soup.title.string)
except Exception as e:
    print('error', e)