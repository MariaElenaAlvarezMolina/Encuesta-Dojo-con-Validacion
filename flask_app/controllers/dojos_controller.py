from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojos import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def proceso():
    if not Dojo.valida_dojo(request.form):
        return redirect ('/')
    else:
        Dojo.guardar(request.form)
        return redirect('/result')

@app.route('/result')
def info():
    dojos = Dojo.muestra_dojos()
    return render_template('info.html', dojos=dojos)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')