from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
xml = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm').read().decode('utf8')
cnt = 0
soup = BeautifulSoup(xml, 'xml')  # делаем суп с помощью lxml
for tag in soup.find_all('tag'):
    if tag['k']=='amenity' and tag['v']=='fuel':
        cnt+=1

fout = open('out4.txt', 'w', encoding='utf8')
print(cnt)
fout.close()
