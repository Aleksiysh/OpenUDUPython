#from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

xml = open('mapcity.osm','r',encoding='utf8').read()
soup = BeautifulSoup(xml,'lxml')
count =0
fout = open('out11.txt','w',encoding='utf8')
for node in soup.find_all('node'):
       print(node['id'],node['lat'],node['lon'],file = fout)
       count+=1
       if count>=100:
              break
fout.close()
pass