from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')  # считываем содержимое
soup = BeautifulSoup(xml, 'xml')  # делаем суп с помощью lxml
cnt1 = 0
cnt2 = 0
for node in soup.find_all('node'):  
    cnt1 += 1
    flag = False
    for tag in node('tag'):
        flag =True
    if flag:
        cnt2+=1
fout = open('out4.txt', 'w', encoding='utf8')
print(cnt1-cnt2, cnt2)
fout.close()
