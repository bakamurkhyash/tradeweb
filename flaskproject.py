from flask import Flask, redirect, render_template, url_for, request, jsonify
from werkzeug.utils import secure_filename
import requests 
import sqlite3
from api import send_request
import json
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("service.html")

@app.route("/delivery")
def delivery():
    return render_template("index.html")


@app.route("/formsubmit", methods = ["POST", "GET"])
def submit():
    if request.method == "POST":
        data = request.form.to_dict(flat=True)
        resp = requests.post("https://n8n-jrp7.onrender.com/webhook-test/1240a920-f11e-497a-a017-135438fc2d80",
                             json = data,
                             headers = {"Content-type": "application/json"},
                              timeout = 10)
        resp.raise_for_status()
        responses = resp.json()
        try:
            return {"status": resp.status_code, "json": resp.json(), "text": resp.text}
            #in above line the 'resp.json()' contains the response from the 'respond to webhook' node
        except ValueError:
            return {"status": resp.status_code, "json": None, "text": resp.text}

@app.post("/file")
def file():
    media = request.files["media"]
    files = {
        "media": (secure_filename(media.filename), media.stream, media.content_type, media.headers)
    }

    data = {
        "from": "delivery"
    }

    resp = requests.post(
        "https://n8n-jrp7.onrender.com/webhook-test/1240a920-f11e-497a-a017-135438fc2d80",
        files = files,
        data = data,
        timeout = 60
    )

    return jsonify({"status": resp.status_code, "text": resp.text}), resp.status_code

if __name__ == "__main__":
    app.run()