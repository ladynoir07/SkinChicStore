from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_session import Session

from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

app= Flask(__name__)
db = SQL("sqlite:///basedatos.db")




@app.route("/")
def index():

    products= db.execute("SELECT * FROM productos")

    return render_template("mostrador.html", products= products)


@app.route("/facial")
def facial():
    a= "maquillaje"
    products= db.execute(
            "SELECT * FROM productos WHERE categoria = ? ", "facial"
        )

    return render_template("facial.html", products= products)

@app.route("/corporal")
def corporal():
    a= "maquillaje"
    products= db.execute(
            "SELECT * FROM productos WHERE categoria = ? ", "corporal"
        )

    return render_template("corporal.html", products= products)

@app.route("/maquillaje")

def maquillaje():
    a= "maquillaje"
    products= db.execute(
            "SELECT * FROM productos WHERE categoria = ? ", "maquillaje"
        )

    return render_template("maquillaje.html", products= products)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("nombre")
        mail = request.form.get("email")
        password = request.form.get("contra")
        confirmation = request.form.get("confirmation")



        hashed_password = generate_password_hash(password)

        try:
            new_user = db.execute(
                "INSERT INTO usuarios (nombre, correo, contraseña) VALUES (?, ?, ?)",
                username,
                mail,
                hashed_password,
            )
        except:
            return warnings.warn("Debe proporcionar una contraseña", Warning)


        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def login():
    """Log user in"""
    if request.method == "POST":
        username = request.form.get("nombre1")
        mail = request.form.get("email1")
        password = request.form.get("contra1")
        rows = db.execute(
            "SELECT * FROM usuarios WHERE username = ?", request.form.get("nombre1")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["contraseña"], request.form.get("contra1")
        ):
            return redirect("/mostrador")

        return redirect("/mostrador")

    else:
        return render_template("register.html")
