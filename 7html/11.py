from urllib.request import urlopen
from bs4 import BeautifulSoup

def getCountInternalLink(link:str):
    response = urlopen(link)
    html = response.read().decode('utf8')
    soup = BeautifulSoup(html, features='html.parser')
    count =0
    for link in soup.findAll('a'):
        if link.has_attr('href'):
            s= link.get('href')
            if s.startswith('/w') and (':' not in s):
                count+=1
    return count


print(getCountInternalLink('https://stepik.org/media/attachments/lesson/258943/Moscow.html'),
    getCountInternalLink('https://stepik.org/media/attachments/lesson/258944/New-York.html'))