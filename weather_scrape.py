
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a brief synopsis of the weather for the next 10 days.
# Include the day, date, high temp, low temp, and chance of rain.
# You can customize the text as you like, but it should be readable
# for the user.  You will need to target specific classes or other
# attributes to pull some parts of the data.
# (e.g.  Wednesday, March 22: the high temp will be 48 with a low of 35, and a 20% chance of rain). (25pts)

from bs4 import BeautifulSoup
import urllib.request

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

my_table = soup.find("table")
rows = my_table.findAll("tr")
header = my_table.findAll("th")

header_list = []
for item in header:
    header_list.append(item.text.strip())
print(header_list)
data_list = []

for i in range(1, len(rows)):
    cells = rows[i].findAll('td')
    row_list = []
    for j in range(len(cells)):
        row_list.append(cells[j].text.strip())
    data_list.append(row_list)
print(data_list)

for i in range(len(data_list)):
    data_list[i].pop(0)
    data_list[i].pop(1)
    data_list[i].pop(-1)
    data_list[i].pop(-1)
print(data_list)

for i in range(len(data_list)):
    print("on", data_list[i][0], "the high/low temperature is", data_list[i][1], "degrees, and the chance of rain is", data_list[i][2])