from flask import Flask, render_template
import os
from os import path
if path.exists("env.py"):
  import env 
SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')


APP = Flask(__name__)

@APP.route('/')
def hello_world():
    return render_template('pages/index.html', title="The Lazy Padwan and his lost Son, and 25 camels, 70 lambs, and young Jesus")

if __name__ == '__main__':
    APP.run(host=os.environ.get('HOSTNAME'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEV'))