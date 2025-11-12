from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env into environment for local dev

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
