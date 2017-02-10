## Testing Arcgis stuff

### Install
> npm install -g geojsonio-cli

> pip install arcgis-rest-query


### Map some stuff

> arcgis-get http://spires2.cityoffrederick.com/ArcGIS/rest/services/BaseCombined/MapServer 0 | /opt/node/bin/geojsonio 



### Join two maps

Base map

> arcgis-get http://spires2.cityoffrederick.com/ArcGIS/rest/services/BaseCombined/MapServer 0 > test.txt 

Flood map

> arcgis-get http://spires2.cityoffrederick.com/ArcGIS/rest/services/Floodplain/MapServer 0 > test2.txt

> cat test.txt | python -mjson.tool > file1.json

> cat test2.txt | python -mjson.tool > file2.json

> cat file2.json > test.json

> cat file1.json >> test.json 

Edit test.json to be proper json with moving the following to the end of the file:

```
    ],
    "type": "FeatureCollection"
}
```

> cat test.json | /opt/node/bin/geojsonio 

Or go to:

[http://geojson.io/](http://geojson.io/)

and add the test.json file.
