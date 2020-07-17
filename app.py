# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html" , time=datetime.now())

@app.route('/results', methods=['GET', 'POST'])

def results():
    #print(user_pokedex)
    dex_number=request.form["pokedex"]
    if dex_number == "1":
        return render_template("results.html",dex_number= dex_number,time=datetime.now())
    elif dex_number == "2":
        return render_template("pokemon2.html",dex_number= dex_number, time=datetime.now()) 
    elif dex_number == "3": 
        return render_template("pokemon3.html",dex_number= dex_number, time=datetime.now())


#@app.route('/pokemon2', methods=['GET', 'POST'])

# def pokemon2():
#     user_pokedex = request.form["pokedex"]
#     #print(user_pokedex)
#     dex_number=request.form["pokedex"]
#     if dex_number == 2:
#         return render_template("pokemon2.html" ,user_pokedex= user_pokedex ,dex_number= dex_number )