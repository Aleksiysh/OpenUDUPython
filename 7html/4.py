from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://stepik.org/media/attachments/lesson/209717/1.html ')
html = response.read().decode('utf8')
print(html)
fout = open('out4.html','w',encoding='utf8')
print(html,file = fout)
fout.close()

soup = BeautifulSoup(html)

for link in soup.find_all('a'):
    print(link) 

pass