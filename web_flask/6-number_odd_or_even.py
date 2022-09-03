#!/usr/bin/python3
"""starts a Flask web app"""


from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(var):
    text = text.replace("_", " ")
    return var

@app.route('/python', defaults={'text': "is_cool"})
@app.route('/python/<text>')
def python(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route('/number')
@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)

@app.route('/number_template')
@app.route('/number_template/<int:n>')
def number_template(n):
    number = "Number: {}".format(n)
    return render_template('5-number.html', number=number)

@app.route('/number_odd_or_even')
@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    if (n % 2 == 0):
        number = "Number: {} is even".format(n)
    else:
        number = "Number: {} is odd".format(n)
    return render_template('6-number_odd_or_even.html', number=number)

app.run(host='0.0.0.0', port=5000)
