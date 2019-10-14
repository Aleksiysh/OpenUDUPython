from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
html = response.read().decode('utf8')
fout = open('out4.html','w',encoding='utf8')
print(html,file = fout)
fout.close()

soup = BeautifulSoup(html)

for link in soup.find_all('a'):
    print(link) 

pass