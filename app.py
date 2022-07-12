from flask import Flask
from utils import load_candidates, get_by_pk

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates()
    candidate_info = ' '
    for candidate in candidates:
        candidate_info += f"<pre> \
                            Имя кандидата - {candidate['name']}\n \
                            Позиция кандидата: {candidate['position']}\n \
                            Навыки через запятую: {candidate['skills']}\n \
                            \n \
                          </pre>"
    return candidate_info


@app.route('/candidates/<int:x>')
def profile(x):
    pk_candidate = get_by_pk(x)
    return pk_candidate

app.run()

if __name__ == '__main__':
    pass
