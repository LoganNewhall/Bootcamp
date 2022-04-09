from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():
    return render_template("dojo.html", dojos = Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<dojo_id>')
def show_dojo(dojo_id):
    data = {
        'dojo_id' : dojo_id
    }
    dojoRecords = Dojo.display_ninjas(data)
    return render_template('dojo_show.html', dojoRecords = dojoRecords)