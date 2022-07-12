from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return f'abcd'


if __name__ == '__main__':
    pass
