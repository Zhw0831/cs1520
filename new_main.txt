import flask
import random
import user
from google.cloud import datastore
from flask import flash, redirect, render_template, request, url_for
from user import get_client
um = user.User_manager()

app = flask.Flask(__name__)
client = get_client()


@app.route('/')
def root():
    return flask.redirect("/s/welcome.html", code=302)

@app.route('/send', methods=['POST','GET'])
def register_user():
    email = flask.request.form['email']
    password = flask.request.form['password']
    age = flask.request.form['age']
    gender = flask.request.form['gender']
   

    um.register(email, password, age, gender) 
    print("You have successfully signed up with email", email)
    return flask.render_template("user.html", email = email, age = age, gender = gender)

# @app.route('/user.html', methods=['POST', 'GET'])
# def personal():
#     return flask.render_template('user.html')

@app.route('/login.html', methods=['POST','GET'])
def login():
    return flask.render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def store_login():
    email = flask.request.form['email']
    password = flask.request.form['password']
    response = um.login(email, password) 
    print(response)

    age = response['age'] 
    gender = response['gender'] 
    return flask.render_template("user.html", email = email, age = age, gender = gender)

@app.route('/signup.html', methods=['POST','GET'])
def signup():
    return render_template('signup.html')


# @app.route('/questions/<id>')
# def questions(id):
#     # TODO fetch data from database, removing the following lanes later
#     choices_ans = []
#     for i in range(101):
#         choices_ans.append(
#             {
#                 "choice": [random.random(), random.random(), random.random(), random.random()]
#             }
#         )

#     return flask.render_template("quiz.html", choices=choices_ans[int(id)],id = id)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)