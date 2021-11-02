import flask
import random
from flask import request
from google.cloud import datastore


app = flask.Flask(__name__)

@app.route('/')
@app.route('/welcome.html')
@app.route('/s/welcome.html')
def root():
    return flask.redirect('/s/welcome.html', code=302)

@app.route('/login.html')
def login():
    return flask.render_template('login.html')

@app.route('/quiz.html')
def quiz():
    return flask.render_template('quiz.html')

@app.route('/submit-form/', method=['GET', 'POST'])
def store():
    result = request.form['getEmail']
    client = datastore.Client()
    ekey = client.key('email', result)
    task = datastore.Entity(key=ekey)
    task["description"] = "New user to email!"
    client.put(task)

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