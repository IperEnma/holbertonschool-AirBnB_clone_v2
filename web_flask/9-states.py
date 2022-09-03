#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.city import City
from models.state import State
from os import getenv



app = Flask(__name__)
app.url_map.strict_slashes = False



@app.teardown_appcontext
def close(exception):
    storage.close()

@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        states = storage.all(State)
        states_list = []
        name_state = ""
        if id is not None:
            for key, state in states.items():
                if state.id == id:
                    states_list.append(state)
                    name_state = state.name
        else:
            for key, state in states.items():
                states_list.append(state)
            states_list.sort(key=lambda x: x.name)
        return render_template("9-states.html", states = states_list, name_state=name_state)
    else:
        cities = storage.all(City)
        states = storage.all(State)
        return render_template("9-states.html", states = states, cities = cities)
app.run(host="0.0.0.0", port=5000)
