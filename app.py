import subprocess

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    ver = subprocess.getoutput('git rev-parse HEAD')
    return ver

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
