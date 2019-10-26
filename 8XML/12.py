from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
fout = open('out12.txt', 'w', encoding='utf8')
xml = urlopen('https://stepik.org/media/attachments/lesson/266078/mapcity.osm').read().decode('utf8')
nodes =list()
soup = BeautifulSoup(xml, 'xml')  # делаем суп с помощью lxml
for way in soup.find_all('way'):
    for node in way('nd'):
        nodes.append(node)
    if nodes[0]['ref'] ==nodes[len(nodes)-1]['ref']:
        
        for tag in way('tag'):
            if tag['k'] == 'building':
                print(way['id'],file = fout)
        
    nodes.clear()
   


# print(cnt)
fout.close()
