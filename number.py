import requests
from flask import Flask
app = Flask(__name__)

url = "https://www.googleapis.com/youtube/v3/channels?id=UC9vUu4vlIlMC0dHQCTvQPbg&key=AIzaSyBJ2K0VZ-Mh1KUsyFW-_y9EL0ZT7dtH8do&part=statistics"

@app.route("/")
def hello():
   r = requests.get(url).json()
   number = r["items"][0]["statistics"]["subscriberCount"]

   return '{"number": ' + number + '}'

app.run()
