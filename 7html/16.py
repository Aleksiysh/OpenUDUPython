from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen(
    ' https://stepik.org/media/attachments/lesson/209723/5.html ')
html = response.read().decode('utf8')
soup = BeautifulSoup(html, features='html5lib')

summ = 0
for var in soup.find_all('td'):
    value = var.text
    summ += int(value)
        
print(summ)        
pass
