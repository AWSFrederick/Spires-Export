from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def hello_world():
    img = requests.get('http://spires2.cityoffrederick.com/ArcGIS/rest/services/Aerial_2014/MapServer/export?bbox=1171900.00012207%2C+622900.000122067%2C+1218100.00012207%2C+669100.000122077&bboxSR=&layers=layers%3Dshow%3A7&layerdefs=&size=1600%2C1200&imageSR=&format=png&transparent=false&dpi=&time=&layerTimeOptions=&f=image')

    return(Flask.response_class(img, mimetype='image/png'))
