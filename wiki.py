from bs4 import BeautifulSoup
import requests
import codecs

__author__ = 'LanAnh'

url = "https://vi.wikipedia.org/wiki/T%E1%BB%89nh_th%C3%A0nh_Vi%E1%BB%87t_Nam"

# get content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
list_province_table = soup.find_all('table')[1]
provinces = []
for row in list_province_table.findAll('tr'):
    try:
        province = row.findAll('td')[1].text
        provinces.append(province)
    except:
        pass

# save
with codecs.open("output", "w", "utf-8") as result_file:
    for province in provinces:
        result_file.write(province)
        result_file.write("\n")
