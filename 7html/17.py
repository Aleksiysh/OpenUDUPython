from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen(
    'https://stepik.org/media/attachments/lesson/258944/New-York.html')
html = response.read().decode('utf8')
soup = BeautifulSoup(html, features='html.parser')

summ = 0
tables = soup.find_all('table', attrs={'class': 'wikitable collapsible collapsed'})

fout = open('out17.html','w',encoding='utf8')
print(tables[1], file=fout)
fout.close()
        
    
pass
