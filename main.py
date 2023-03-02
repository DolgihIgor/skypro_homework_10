from flask import Flask


app = Flask(__name__)


@app.route("/")
def page_index():
    return "Наша страничка!"


app.run(host="127.0.0.1", port=8080)