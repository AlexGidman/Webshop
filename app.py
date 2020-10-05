from flask import Flask, render_template, request, redirect, url_for
import pdb
import 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/item/new", methods=["GET", "POST"])
def new_item():
    # pdb.set_trace() # stops package here to inspect post request
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        return render_template("new_item.html")