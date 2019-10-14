from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')
html = response.read().decode('utf8')

soup = BeautifulSoup(html)

codes = {}
for code in soup.find_all('code'):
    s =code.text
    if s not in codes:
        codes[s] = 0
    codes[s]+=1  
max = 0  
maxCode = list()    
for var in codes:
    if codes[var]>max:
        maxCode.clear()
        max = codes[var]
    if codes[var] == max:
        maxCode.append(var)   

print(' '.join(sorted(maxCode)))         
pass