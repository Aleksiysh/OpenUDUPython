from bs4 import BeautifulSoup

xml = open('map.osm','r',encoding='utf8').read()

soup = BeautifulSoup(xml,'lxml')
#print(soup)
for node in soup.find_all('node'):
    for tag in node('tag'):
        print(tag)
pass