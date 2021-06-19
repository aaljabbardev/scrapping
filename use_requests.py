import requests
from bs4 import BeautifulSoup

try:
    url = 'http://www.jadwalsholat.pkpu.or.id/?id=58'
    r = requests.get(url)
    # print(r.text)
    soup = BeautifulSoup(r.text, features="html.parser")
    # print(soup.title.string)
    data = soup.find_all('tr', 'table_highlight')[0]

    sholat = {}
    i = 0
    for d in data:
        if i > 0:
            if i == 1:
                sholat['subuh'] = d.get_text()
            elif i == 2:
                sholat['dzuhur'] = d.get_text()
            elif i == 3:
                sholat['ashar'] = d.get_text()
            elif i == 4:
                sholat['maghrib'] = d.get_text()
            elif i == 5:
                sholat['isya'] = d.get_text()
        i += 1

    # sholat = sorted(sholat.items(), key=lambda x: x[1], reverse=False)
    print(sholat['subuh'])
except Exception as e:
    print('error', e)
