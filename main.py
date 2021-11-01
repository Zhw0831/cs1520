import flask
import random

app = flask.Flask(__name__)


@app.route('/')
def root():
    return flask.redirect("/s/login.html", code=302)


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
