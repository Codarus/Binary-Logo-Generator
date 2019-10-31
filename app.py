from flask import Flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/generator')
def g_handler():

    return render_template("generator.html")


if __name__ == '__main__':
    app.run()
