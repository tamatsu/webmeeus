from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import pymeeus
import pymeeus.Sun
import pymeeus.Epoch
import datetime
import math
from dateutil import tz

@app.route('/')
def hello_world():
    now = datetime.datetime.utcnow()
    jp_begin = datetime.datetime.combine((now + datetime.timedelta(hours=9)).date(), datetime.datetime.min.time()) + datetime.timedelta(hours=-9)
    jp_end = jp_begin + datetime.timedelta(days=1)
    apparent_lon, r = pymeeus.Sun.Sun.apparent_longitude_coarse(pymeeus.Epoch.Epoch(now))
    jp_begin_lon, r = pymeeus.Sun.Sun.apparent_longitude_coarse(pymeeus.Epoch.Epoch(jp_begin))
    jp_end_lon, r = pymeeus.Sun.Sun.apparent_longitude_coarse(pymeeus.Epoch.Epoch(jp_end))

    return jsonify({
        "longitude": float(apparent_lon),
        "jp_begin_lon": float(jp_begin_lon),
        "jp_end_lon": float(jp_end_lon)
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)