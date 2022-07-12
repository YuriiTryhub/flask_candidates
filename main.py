from flask import Flask
from utils import load_candidates

app = Flask(__name__)


@app.route('/')
def page_index():
    return f"<pre> \
                Имя кандидата -\n \
                Позиция кандидата\n \
                Навыки через запятую\n \
                \n \
                Имя кандидата -\n \
                Позиция кандидата\n \
                Навыки через запятую\n \
                \n \
                Имя кандидата -\n \
                Позиция кандидата\n \
                Навыки через запятую\n \
             </pre>"

app.run()

if __name__ == '__main__':
    pass
