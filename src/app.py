import os
from flask import Flask


app = Flask(__name__)

@app.route("/ruok")
def ruok():
    print(f"CUSTOM_ENV_VAR = {os.environ['CUSTOM_ENV_VAR']}")
    return "imok"
