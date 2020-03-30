from bs4 import BeautifulSoup
from pprint import pprint
import requests

url = "https://www.mohfw.gov.in/#cases"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

div = soup.find("div", {"class": "content newtab"})
table = div.find("div", {"class": "table-responsive"})

data = dict()

for row in table.find_all('tr'):
    col_data = []
    for col in row.find_all('td'):
        col_data.append(col.text)
    try:
        print(col_data)
        data[col_data[1]] = {
            'total': col_data[0],
            'cured': col_data[2],
            'deaths': col_data[3]
        }
    except:
        pass

pprint(data)
