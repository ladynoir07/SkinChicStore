from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = '123'

usuarios = {
    'usuario1': {'username': 'usuario1', 'password_hash': generate_password_hash('password1')},
    'usuario2': {'username': 'usuario2', 'password_hash': generate_password_hash('password2')}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            usuario = usuarios.get(username)
            if usuario and check_password_hash(usuario['password_hash'], password):
                session['user_id'] = username
                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('index'))
            else:
                flash('Usuario o contraseña incorrectos', 'error')
        else:
            flash('Debe proporcionar un usuario y una contraseña', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
