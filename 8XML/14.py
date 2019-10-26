from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

xml = urlopen(
    'https://stepik.org/media/attachments/lesson/266078/mapcity.osm').read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')
dictNodes = {}
fout = open('out14.txt', 'w', encoding='utf8')
for node in soup.find_all('node'):
    dictNodes[node['id']] = (float(node['lat']), float(node['lon']))

nds = []
nodes = []
for way in soup.find_all('way'):
    for node in way('nd'):
        nodes.append(node['ref'])
    if nodes[0] == nodes[len(nodes)-1]:
        flag = False
        for tag in way('tag'):
            if tag['k'] == 'building':
                flag = True
                if flag:
                    print(way['id'],file =fout)
                    for nd in nodes:
                        nds.append(dictNodes[nd])
                    print(nds,file =fout)
                nds.clear()

                      #       print(dictNodes[way['id']] )
    nodes.clear()
fout.close()
pass
