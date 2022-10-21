from distutils.command.build import build
import os
from pathlib import Path
from flask import Flask
from flask import send_file
from flask import Response
import json
from fan import Fan


app = Flask(__name__)
bedroom_fan = Fan()


@app.route("/")
def hello_world():
    bedroom_fan.toggle_light()
    return json.dumps(bedroom_fan.toggle_light(), indent=4)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)