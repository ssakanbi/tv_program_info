from flask import Flask, render_template, request, jsonify
import json
import requests
from pprint import pprint
import requests_cache

app = Flask(__name__)
tv_maze_url = 'http://api.tvmaze.com/singlesearch/shows?q={tv_show_name}'

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/tv', methods=['POST','GET'])
def tvshow():
    tv_show_name = request.form['text']
    tv_show_name = request.args.get('tv_show_name', tv_show_name)
    tv_url = tv_maze_url.format(tv_show_name=tv_show_name)
    resp = requests.get(tv_url)
    a = resp.json()
    return render_template("tv.html",final=a)
if __name__=="__main__":
    app.run(port=8080, debug=True)
