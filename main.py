from flask import Flask
from utils import load_candidates

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates()
    page_text = "<pre>"
    for candidate in candidates.values():
        page_text += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    page_text += "</pre>"
    return page_text


@app.route("/candidates/<int:id>")
def page_candidates(id):
    candidates = load_candidates()
    candidate = candidates[id]
    page_text = f"<pre><img src={candidate['picture']}>\n\n{candidate['name']}\n{candidate['position']}\n{candidate['skills']}</pre>"
    return page_text


@app.route("/skill/<skill>")
def page_skill(skill):
    candidates = load_candidates()
    page_text = "<pre>\n"
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        print(candidate_skills)
        if skill in candidate_skills:
            page_text += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
            print(candidate)
    page_text += "</pre>"
    print(page_text)
    return page_text


app.run(host="127.0.0.2", port=8080)
