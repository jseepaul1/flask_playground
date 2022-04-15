from os import times
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def level_one():
    return render_template("index.html", box="box-1", times=3, color="blue")

@app.route('/play/<int:x>')
def level_two(x):
    return render_template("index.html", box="box-1",times=x, color="blue")

@app.route('/play/<int:x>/<string:color>')
def level_three(x, color):
    print("color - ", color)
    return render_template("index.html", box="box-1",times=x, color=color)


if __name__ == "__main__":
    app.run(debug=True)
