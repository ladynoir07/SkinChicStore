from werkzeug.security import check_password_hash, generate_password_hash

# ...

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Debe proporcionar un nombre de usuario", 403)

        elif not request.form.get("password"):
            return apology("Debe proporcionar una contraseña", 403)

        rows = db.execute(
            "SELECT * FROM usuarios WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("Nombre de usuario y/o contraseña inválidos", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Debe ingresar un nombre")

        if not password:
            return apology("Debe ingresar una contraseña")

        if not confirmation:
            return apology("Debe ingresar su contraseña")

        if password != confirmation:
            return apology("Las contraseñas no coinciden")

        hashed_password = generate_password_hash(password)

        try:
            new_user = db.execute(
                "INSERT INTO usuarios (username, password) VALUES (?, ?)",
                username,
                hashed_password,
            )
        except:
            return apology("El nombre de usuario ya existe")

        session["user_id"] = new_user
        return redirect("/")
