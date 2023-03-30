from matplotlib.font_manager import json_load
from flask import Flask, render_template

import json

app = Flask(__name__)

fil_meny = open("meny.json")
meny = json.load(fil_meny)
fil_meny.close()


fil_handlekurv = open("handlekurv.json")
handlekurv = json.load(fil_handlekurv)
fil_handlekurv.close()



def skriv_handlekurv():
    fil_handlekurv = open("handlekurv.json", "w")
    json.dump(handlekurv, fil_handlekurv)
    fil_handlekurv.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meny")
def rute_meny():
    return render_template("meny.html", meny=meny)

@app.route("/hjemlevering")
def rute_hjemlevering():
    return render_template("hjemlevering.html")

@app.route("/omoss")
def rute_omoss():
    return render_template("omoss.html")

@app.route("/menyen/<id>")
def rute_menyen(id):
    menyen = meny[id]
    return render_template("menyen.html", id=id, menyen=menyen)

@app.route("/meny/<kategori>")
def rute_sortering(kategori):
    sortert = {}
    for id, menyen in meny.items():
        if menyen["kategori"] == kategori:
            sortert[id] = menyen
    return render_template("meny.html", meny=sortert )

@app.route("/menyen/<id>/legg-til")
def rute_legg_til(id):
    handlekurv.append(id)
    skriv_handlekurv()
    return rute_menyen(id)

@app.route("/handlekurv")
def rute_handlekurv():
    return render_template("handlekurv.html", handlekurv=handlekurv, meny=meny)

@app.route("/handlekurv/slett/<id>")
def rute_slett(id):
    handlekurv.remove(id)
    skriv_handlekurv()
    return rute_handlekurv()
