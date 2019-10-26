from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import math


def getsqr(coordlist):
    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen,
                         (now[1] - baselon) * degreelen * math.sin(baselat)))
    sqr = 0
    for i in range(len(newcoord) - 1):
        sqr += newcoord[i][0] * newcoord[i + 1][1] - \
            newcoord[i + 1][0] * newcoord[i][1]
    sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
    return abs(sqr)


idMax = ''
maxSqr = 0

xml = urlopen(
    'https://stepik.org/media/attachments/lesson/266078/mapcity.osm').read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')
dictNodes = {}
fout = open('out15.txt', 'w', encoding='utf8')
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
                    print(way['id'], file=fout)
                    for nd in nodes:
                        nds.append(dictNodes[nd])
                    if getsqr(nds) > maxSqr:
                        maxSqr = getsqr(nds)
                        idMax = way['id']
                    print(nds, file=fout)
                nds.clear()
    nodes.clear()
fout.close()
print(idMax)
pass
