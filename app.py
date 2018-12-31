import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    path = os.path.dirname(os.path.abspath(__file__))

    with open('%s/.git/refs/heads/master' % path) as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
