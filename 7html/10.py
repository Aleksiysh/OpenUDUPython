from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
html = response.read().decode('utf8')
soup = BeautifulSoup(html, features='html.parser')
count =0
a_set = set()
a_set1 = set()
for link in soup.findAll('a'):
    if link.has_attr('href'):
        s= link.get('href')
        if s.startswith('/w') and (':' not in s):
            a_set.add(s)
            count+=1
        if s.startswith('/') and (':' not in s):
            a_set1.add(s)

difset = set(a_set1-a_set)

pass
        


print(len(a_set),count)