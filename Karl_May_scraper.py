

from gettext import find
from ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER
from urllib import request
from requests_html import HTMLSession

from bs4 import BeautifulSoup
from openpyxl import Workbook



wb= Workbook()
ws = wb.active

ws.title = "Karl_May"

url = "https://www.printrecarti.ro/?cauta=karl+may"



html = request.urlopen(url).read().decode('utf8')


html[:60]

soup = BeautifulSoup(html, 'html.parser')

test=soup.find_all('span', class_="titlull")
#lk= soup.find_all('div', class_="produs ll1col")

"""for i in test:
    title= i.find('a')

    app=title.text.strip()

    ws.append([app])
    
    
    #print(title.text.strip())"""


for j in range(1,20):
    url2= f"https://www.printrecarti.ro/acasa/?cauta=karl+may&p={j}"

    test2= soup.find_all('span', class_="titlull")

    for k in test2:
        tilu= k.find('a')
        app=tilu.text.strip()
        print(tilu.text.strip())
        ws.append([app])



wb.save("Karl_May_scraped_data.xlsx")