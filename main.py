from flask import Flask
from utils import load_candidates

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates()
    page_text = "<pre>"
    for candidate in candidates.items():
        page_text += f'{candidate[1]["name"]}\n{candidate[1]["position"]}\n{candidate[1]["skills"]}\n\n'
    page_text += "</pre>"
    return page_text


@app.route("/candidates/<int:id>")
def page_candidates(id):
    candidates = load_candidates()
    candidate = candidates[id]
    page_text = f"<pre><img src={candidate['picture']}>\n\n{candidate['name']}\n{candidate['position']}\n{candidate['skills']}</pre>"
    return page_text


app.run(host="127.0.0.2", port=8080)
