from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
from dotenv import load_dotenv
import redis
import nasapy
import os
import json
import datetime


'''REDIS_START'''

r = redis.Redis(host='localhost', port=6379, db=2)

'''REDIS_END'''

load_dotenv()

API_KEY_NASA = os.getenv('API_NASA_KEY')

nasa = nasapy.Nasa(key=API_KEY_NASA)

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/archiv_nasa/api/v1.0/photo_of_the_day/', methods = ['GET'])
def photo_of_the_day():

    today = f"{datetime.datetime.now():%Y-%m-%d}"

    if r.get(today):
        print('Рботает кеш редиса')
        return jsonify(json.loads(r.get(today)))

    else:

        inf = nasa.picture_of_the_day()

        key_for_r = 0

        for key in inf:
            if (key == 'date'):
                key_for_r = inf[key]

        json_inf = json.dumps(inf)

        r.set(key_for_r, json_inf)

        print('Данные занесены в редис')

        return jsonify(inf)


@app.route('/archiv_nasa/api/v1.0/photo_of_define_day/<int:year>-<int:month>-<int:day>', methods = ['GET'])
def photo_of_define_day(year, month, day):

    date = f"{year}-{month}-{day}"

    today = f"{datetime.datetime.now():%Y-%m-%d}"

    if date == today:
        return redirect(url_for('photo_of_the_day'))

    elif r.get(date):
        print('Рботает кеш редиса')
        return jsonify(json.loads(r.get(date)))

    else:

        inf = nasa.picture_of_the_day(f'{date}', hd=True)

        key_for_r = 0

        for key in inf:
            if (key == 'date'):
                key_for_r = inf[key]

        json_inf = json.dumps(inf)

        r.set(key_for_r, json_inf)

        print('Данные занесены в редис')

        return jsonify(inf)


@app.route('/archiv_nasa/api/v1.0/all_dates', methods=['GET'])
def all_dates_in_system():

    list_date = []

    all_dates = {}

    keys = r.keys()

    counter = 0

    for k in keys:
        name_of_key = k.decode('utf-8')
        list_date.append(name_of_key)
        # all_dates[counter] = name_of_key
        # counter = counter + 1

    list_date.sort(reverse=True)


    for date in list_date:
        all_dates[counter] = date
        counter = counter + 1
        
    return jsonify(all_dates)



if __name__ == '__main__':
    app.run(debug=True)