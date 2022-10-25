from distutils.command.build import build
import os
from pathlib import Path
from flask import Flask
from flask import send_file
from flask import Response
from flask import request
import json
from fan import Fan


app = Flask(__name__)
bedroom_fan = Fan()


@app.route("/status")
def get_status():
    return bedroom_fan.get_status_fan()

@app.route("/status", methods=['POST'])
def set_status():
    req = request.json
    return bedroom_fan.set_status(req)

@app.route("/light")
def hello_world():
    response = bedroom_fan.toggle_light()
    print(response)
    return json.dumps(response, indent=4)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)