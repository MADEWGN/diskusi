from flask import *
import json
from deta import Deta 

app = Flask(__name__)

@app.route("/")
def index():
    return "Halo Dunia !"

@app.route("/login")
def login():
    return "Login"

# make register page

