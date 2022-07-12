from flask import Flask
from utils import load_candidates, get_by_pk, get_by_skill, url

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates()
    candidate_info = ' '
    for candidate in candidates:
        candidate_info += f"""<img src='({url})'> \n
                          <pre> \n
                            {candidate['name']}\n
                            {candidate['position']}\n
                            {candidate['skills']}\n
                            \n
                          </pre>"""
    return candidate_info


@app.route('/candidates/<int:x>')
def profile(x):
    pk_candidate = get_by_pk(x)
    return pk_candidate


@app.route('/skills/<x>')
def by_skill_profile(x):
    candidate_skill = get_by_skill(x)
    return candidate_skill


app.run()

if __name__ == '__main__':
    pass
