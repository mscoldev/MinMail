from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from controllers.db import getUser
from models.Message import *
import sqlite3 as sql
from decouple import config



#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User
# Inicializando la aplicacion

app = Flask(__name__)

db = config('DATABASE_NAME')

@app.route('/')
# renderizamos el archivo HTML que se encuentra en la carpeta Templates
def index():
    data = {
        'title': 'Inicio Login'
    }

    return redirect(url_for('login'))
    # return render_template('login.html', data=data)

@app.route('/login', methods=['POST','GET'])
def login():
    data = {
        'title': 'Inicio Login'
    }
    if request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        user = User(request.form['password'],request.form['email'])
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('inbox'))
            else: 
                flash('Invalid Password...')
                return redirect(url_for('login'))
        else:
            flash('User not found ...')
            return render_template('/auth/login.html', data=data)
    else:
        return render_template('/auth/login.html', data=data)
    
@app.route('/send')
def send_mails():
    data = {
        'title': 'Send Mail'
    }
    return render_template('send.html', data=data)

@app.route('/recovery')
def recovery():
    data = {
        'title': 'Recuperar contrasena'
    }
    return render_template('recovery.html', data=data)


@app.route('/send/mail', methods=['POST'])
def send_mail():
    try:
        to = request.form["to"]
        subject = request.form["subject"]
        msg= request.form["msg"]
        message = Message(to, subject, msg)
        
        return jsonify(message.serialize()),200
    except Exception: 
        print("Error")
        return('Error - Algo ha salido mal'), 500

@app.route('/inbox', methods=['GET'])
def inbox():
    return render_template('inbox.html', data=data)

def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))  # Redireccionar a otra pagina


if __name__ == '__main__':
    # Creacion de enlace por medio de una regla directa app.add_url_rule
    # app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    # Inicio de la apliacion
    app.run(debug=True, port=5000)
