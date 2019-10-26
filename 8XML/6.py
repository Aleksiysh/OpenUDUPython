from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
xml = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm').read().decode('utf8')
#xml = open('map2 (2).osm', 'r', encoding='utf8')
# xml = resp.read()#.decode('utf8')  # считываем содержимое
soup = BeautifulSoup(xml, 'xml')  # делаем суп с помощью lxml
maxWayId = -1
maxLen = 0
for node in soup.find_all('way'):
    if len(node("nd"))>maxLen:
        maxLen = len(node('nd'))
        maxWayId = node['id']
fout = open('out4.txt', 'w', encoding='utf8')
print(maxWayId,maxLen)
fout.close()
