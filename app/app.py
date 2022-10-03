from flask import Flask, render_template, request, redirect, url_for, jsonify
from controllers.db import getUser
from models.Message import *

# Inicializando la aplicacion

app = Flask(__name__)

# Creacion de un enlace por medio de un decorador @app.route('/')


@app.before_request
def before_request():
    print("Antes de la peticion")


@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response


@app.route('/')
# renderizamos el archivo HTML que se encuentra en la carpeta Templates
def index():
    cursos = ['PHP', 'Python', 'Java', 'JavaScript']
    data = {
        'title': 'Inicio Login',
        'wellcome': 'Saludos!',
        'cursos': cursos,
        'length': len(cursos)
    }
# Enviamos la data al archivo HTML
    return render_template('login.html', data=data)


@app.route('/contactos/<nombre>')
def contactos(nombre):
    data = {
        'title': 'Contacto',
        'nombre': nombre
    }
    return render_template('contacto.html', data=data)


@app.route('/send')
def send_mails():
    data = {
        'title': 'Send Mail'
    }
    return render_template('send.html', data=data)


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

@app.route('/usuario')
def usuario():
    user = getUser('maser84')
    return jsonify(user)


# Un link directo ->


def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))  # Leer parametros desde una peticion
    print(request.args.get('param2'))
    return 'OK'


def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))  # Redireccionar a otra pagina


if __name__ == '__main__':
    # Creacion de enlace por medio de una regla directa app.add_url_rule
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    # Inicio de la apliacion
    app.run(debug=True, port=5000)
