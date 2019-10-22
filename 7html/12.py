from urllib.request import urlopen
from bs4 import BeautifulSoup

def getSetInternalLink(link:str):
    rezSet = set()
    response = urlopen(link)
    html = response.read().decode('utf8')
    soup = BeautifulSoup(html, features='html.parser')
    count =0
    for link in soup.findAll('a'):
        if link.has_attr('href'):
            s= link.get('href')
            if s.startswith('/w') and (':' not in s):
                rezSet.add(s)
    return rezSet



print(len(getSetInternalLink('https://stepik.org/media/attachments/lesson/258943/Moscow.html')&
    getSetInternalLink(' https://stepik.org/media/attachments/lesson/258944/New-York.html')))