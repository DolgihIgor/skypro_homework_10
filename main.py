from flask import Flask
from utils import load_candidates

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates()
    page_text = "<pre>"
    for i in candidates.items():
        page_text += f'{i[1]["name"]}\n{i[1]["position"]}\n{i[1]["skills"]}\n\n'
    page_text += "</pre>"
    return page_text


app.run(host="127.0.0.1", port=8080)
