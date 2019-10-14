from urllib.request import urlopen
from bs4 import BeautifulSoup


def getHomeLink(link):
    response = urlopen(link)
    html = response.read().decode('utf8')
    soup = BeautifulSoup(html,features='html.parser')
    res = set()
    for var in soup.find_all('a'):
        if var.has_attr('href'):
            s = var.get('href')
            if s.startswith('/') \
                and ':' not in s \
                    and not s.startswith('//'):
                res.add(s)
    return res


set1 = getHomeLink(
    ' https://stepik.org/media/attachments/lesson/258943/Moscow.html')
set2 = getHomeLink(
    'https://stepik.org/media/attachments/lesson/258944/New-York.html ')

res = sorted(list(set1 & set2))
fout = open('out13.txt', 'w', encoding='utf8')
for var in res:
    print(var, file=fout)
fout.close()

pass
