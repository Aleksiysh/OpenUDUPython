from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
xml = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm').read().decode('utf8')
soup = BeautifulSoup(xml, 'xml')  # делаем суп с помощью lxml
cnt = 0
for node in soup.find_all('node'):
    for tag in node('tag'):
        if tag['k']=='amenity' and tag['v']=='fuel':
            cnt+=1

fout = open('out4.txt', 'w', encoding='utf8')
print(cnt)
fout.close()
