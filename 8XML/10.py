from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
minlon, minlat, maxlon, maxlat = (37.5649, 55.5586, 37.5803, 55.5728)
# скачиваем файл
url = ('https://www.openstreetmap.org/api/0.6/map?bbox=' +
       str(minlon) + '%2C' +
       str(minlat)+'%2C' +
       str(maxlon)+'%2C' +
       str(maxlat))
urlretrieve(url, 'out10.osm')

