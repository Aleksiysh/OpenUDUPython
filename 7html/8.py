from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://stepik.org/media/attachments/lesson/258939/webpage.html')
html = response.read().decode('utf8')
fout = open('out8.html','w',encoding='utf8')
#print(html,file = fout)


soup = BeautifulSoup(html)

for link in soup.find_all('a'):
    if link.has_attr('href'):
        s =link.get('href')
        if s.startswith('http://') or s.startswith('https://'):
            print(s,file = fout)
fout.close()
pass