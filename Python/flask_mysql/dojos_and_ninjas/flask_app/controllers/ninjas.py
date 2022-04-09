from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos = Dojo.get_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
        'dojo_id' : request.form['dojo_id'],
        'f_name' : request.form['f_name'],
        'l_name' : request.form['l_name'],
        'age' : request.form['age']
    }
    Ninja.save(data)
    return redirect(f"/dojos/{request.form['dojo_id']}")