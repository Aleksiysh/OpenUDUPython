from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml
cnt = 0
for way in soup.find_all('node'): # идем по всем тэгам way
    cnt += 1 # и просто считаем их количество

fout = open('out4.txt','w',encoding='utf8')
print(cnt,file = fout)
fout.close()