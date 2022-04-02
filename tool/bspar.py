import sys
import time
from bs4 import BeautifulSoup

print(sys.argv)
if len(sys.argv) == 1:
    filename = input()
else:
    filename = sys.argv[1]

soup = BeautifulSoup(open(filename,encoding='utf8'), "html5lib")
h1 = soup.find('h1')
date = soup.find('time')['datetime']
date = '.'.join(date.split('-'))
#print(date)

home = BeautifulSoup(open("../index.html",encoding='utf8'), "html5lib")
original_tag = home.ul
new_li = home.new_tag("li")
original_tag.insert(1,new_li)
original_tag = home.ul.li
new_a = home.new_tag("a", href=filename)
new_a.string = '(%s)%s' % (date, h1.get_text())
original_tag.insert(1,new_a)

#print(str(home))

with open('index.html', 'w', encoding='utf8') as indexfile:
    indexfile.write(home.prettify())
