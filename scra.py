html = '''<body>
<p>Blah text</p>
<div class="tracklistInfo">
<p class="artist">Diplo - Justin Bieber - Skrillex</p>
<p>Where Are U Now</p>
</div>
</body>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

for track in soup.find_all(class_='tracklistInfo'):
    print(track.find_all('p')[0].text)
    print(track.find_all('p')[1].text)

import requests

URL = "https://www.anwb.nl/verkeer/flitsers"

r = requests.get(URL)

html = r.text

soep = BeautifulSoup(html, 'html.parser')

print (soep.prettify())

for road in soep.find_all('div', class_='traffic-list-road-counter'):
    print('found one')
    print(road.find_all('span')[0].text)


