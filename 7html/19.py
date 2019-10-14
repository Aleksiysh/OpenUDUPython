def tbodyToCsv(table,fout):
    data = []
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    for row in data:
        print(','.join(row),file = fout)


from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen(
    'https://stepik.org/media/attachments/lesson/258944/New-York.html')
html = response.read().decode('utf8')
soup = BeautifulSoup(html, features='html.parser')

summ = 0
tables = soup.find_all(
    'table', attrs={'class': 'wikitable collapsible collapsed'})
fout = open('19.csv','w',encoding='utf8')
for i in range(3):
    tbodyToCsv(tables[i],fout)
    print('', file=fout)
fout.close()    


pass
