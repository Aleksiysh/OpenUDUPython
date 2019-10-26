from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
fout = open('out13.txt', 'w', encoding='utf8')
xml = urlopen(
    'https://stepik.org/media/attachments/lesson/266078/mapcity.osm').read().decode('utf8')
nodes = list()
soup = BeautifulSoup(xml, 'xml')  # делаем суп с помощью lxml
for way in soup.find_all('way'):
    for node in way('nd'):
        nodes.append(node['ref'])
    if nodes[0] == nodes[len(nodes)-1]:
        flag = False
        for tag in way('tag'):
            if tag['k'] == 'building':
                flag = True
                if flag:
                    print(way['id'], file=fout)
                    print(*nodes, file=fout)
    nodes.clear()
fout.close()
