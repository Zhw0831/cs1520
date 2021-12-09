import flask
import random
from flask import request
from google.cloud import datastore


app = flask.Flask(__name__)

def get_client():
    return datastore.Client()

def create_thing():
    client = get_client()
    key = client.key('User')
    return datastore.Entity(key)

def update_thing(thing):
    client = get_client()
    client.put(thing)

@app.route('/')
def root():
    return flask.redirect('/s/welcome.html', code=302)

@app.route('/login.html', methods=['GET','POST'])
def login():
    return flask.render_template('login.html')

@app.route('/signup.html', methods=['GET','POST'])
def signup():
    return flask.render_template('signup.html')

@app.route('/user.html', methods=['POST', 'GET'])
def personal():
    return flask.render_template('user.html')

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

@app.route('/login', methods=['GET', 'POST'])
def store():
    email = flask.request.form['email']
    password = flask.request.form['password']
    thing = create_thing()
    thing['email'] = email
    thing['password'] = password
    update_thing(thing)
    return root()

@app.route('/send', methods=['GET', 'POST'])
def register_user():
    email = flask.request.form['email']
    password = flask.request.form['password']
    age = flask.request.form['age']
    gender = flask.request.form['gender']
   
    thing = create_thing()
    thing['email'] = email
    thing['password'] = password
    thing['age'] = age
    thing['gender'] = gender
    update_thing(thing)
    print("You have successfully signed up with email", email)
    return flask.render_template("user.html", email = email, age = age, gender = gender)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)