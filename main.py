import flask
import random
from flask import request
from google.cloud import datastore


app = flask.Flask(__name__)

@app.route('/')
def root():
    return flask.redirect('/s/welcome.html', code=302)

@app.route('/login.html')
def login():
    return flask.render_template('login.html')

@app.route('/questions/<id>')
def questions(id):
    # TODO fetch data from database, removing the following lanes later
    choices_ans = []
    for i in range(101):
        choices_ans.append(
            {
                "choice": [random.random(), random.random(), random.random(), random.random()]
            }
        )

    return flask.render_template("quiz.html", choices=choices_ans[int(id)],id = id)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
