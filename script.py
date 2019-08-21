#! usr/bin/env python

from sys import argv
from os.path import exists
import simplejson as json

script, csvjson, out_file = argv

data = json.load(open(csvjson))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["BEGIN_LAT"], d["BEGIN_LON"]],
            },
        "properties" : d,
     } for d in data]
}


output = open(out_file, 'w')
json.dump(geojson, output)

print (geojson)