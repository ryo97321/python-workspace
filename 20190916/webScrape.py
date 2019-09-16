import requests
import json
from bs4 import BeautifulSoup

r = requests.get('https://nikkei225jp.com/chart/')
text = r.text

date = text.split('<div class=wtimeT>')[1].split('</div>')[0]
nikkei = text.split('<div class=if_cur>')[1].split('</div>')[0].replace(',', '')
dau = text.split('<div class=if_cur>')[2].split('</div>')[0].replace(',', '')
kawase = text.split('<div class=if_cur>')[3].split('</div>')[0].replace(',', '')

print('今日は', date, 'です')
print('日経株価は', nikkei, '円です')
print('ダウ平均株価は', dau, '円です')
print('為替ドルは', kawase, '円です')

a = open('shares.csv', 'w')
a.write('日時,日経平均株価,ダウ平均株価,為替ドル\n')
a.write(date+','+nikkei+','+dau+','+kawase+'\n')
a.close()

soup = BeautifulSoup(r.text, "html.parser")

for a in soup.find_all('a'):
    if 'http' in str(a):
        print(a.text)
        print(a.attrs['href'])
