from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')
html = response.read().decode('utf8')
print('Python' if html.count('Python')>html.count('C++') else 'C++')


