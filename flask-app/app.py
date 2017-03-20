from flask import Flask
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/maptorender/MapServer/export?bbox=1189970.24945014%2C637070.413482656%2C1210045.399164%2C645541.933225805&bboxSR=&layers=&layerdefs=&size=1600%2C1200&imageSR=&format=png&transparent=false&dpi=&time=&layerTimeOptions=&f=image'

@app.route('/')
def mapurls():
    url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/'
    maps = requests.get(url)
    encoding = maps.encoding if 'charset' in maps.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(maps.content, from_encoding=encoding)
    
    map_links = []
    for link in soup.find_all('a', href=True):
        if "MapServer" in link['href']:
            map_links.append(link['href'])

    #print(map_links)
    new_map_links = []
    for map_link in map_links:
        new_map_links.append(
            '<a href="http://127.0.0.1:5000/export/%s">%s</a><br>' % (map_link.replace('/ArcGIS/rest/services/','').replace('/MapServer', ''), map_link.replace('/ArcGIS/rest/services/','').replace('/MapServer', ''))
        )
    return('\n'.join(new_map_links))

@app.route('/export/<map>')
def export(map):
    img = requests.get(url.replace('maptorender', map))
    return(Flask.response_class(img, mimetype='image/png'))
