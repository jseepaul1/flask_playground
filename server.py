from os import times
from flask import Flask, render_template
app = Flask(__name__)

# When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes. Please use a template to render this.
@app.route('/play')
def level_one():
    return render_template("index.html", box="box-1", times=3, color="blue")

# When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times.
#  For example, localhost:5000/play/7 should display these blue boxes 7 times. Calling localhost:5000/play/35 would display these blue boxes 35 times.
@app.route('/play/<int:x>')
def level_two(x):
    return render_template("index.html", box="box-1",times=x, color="blue")

# When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color). 
@app.route('/play/<int:x>/<string:color>')
def level_three(x, color):
    print("color - ", color)
    return render_template("index.html", box="box-1",times=x, color=color)


if __name__ == "__main__":
    app.run(debug=True)
