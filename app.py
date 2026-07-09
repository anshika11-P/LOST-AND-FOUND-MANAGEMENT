from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE ----------------

def get_connection():
    conn = sqlite3.connect("lostfound.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users(name,email,password) VALUES(?,?,?)",
                (name, email, password)
            )
            conn.commit()
            conn.close()

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            conn.close()
            return "Email already exists!"

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Email or Password"

    return render_template("login.html")
# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- REPORT LOST ITEM ----------------

@app.route("/report_lost", methods=["GET", "POST"])
def report_lost():

    if request.method == "POST":

        item_name = request.form["item_name"]
        description = request.form["description"]
        location = request.form["location"]
        date = request.form["date"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO lost_items
            (item_name, description, location, date)
            VALUES (?, ?, ?, ?)
            """,
            (item_name, description, location, date)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("lost_items"))

    return render_template("report_lost.html")


# ---------------- REPORT FOUND ITEM ----------------

@app.route("/report_found", methods=["GET", "POST"])
def report_found():

    if request.method == "POST":

        item_name = request.form["item_name"]
        description = request.form["description"]
        location = request.form["location"]
        date = request.form["date"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO found_items
            (item_name, description, location, date)
            VALUES (?, ?, ?, ?)
            """,
            (item_name, description, location, date)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("found_items"))

    return render_template("report_found.html")
# ---------------- VIEW LOST ITEMS ----------------

@app.route("/lost_items")
def lost_items():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM lost_items ORDER BY id DESC")
    items = cursor.fetchall()

    conn.close()

    return render_template("lost_items.html", items=items)


# ---------------- VIEW FOUND ITEMS ----------------

@app.route("/found_items")
def found_items():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM found_items ORDER BY id DESC")
    items = cursor.fetchall()

    conn.close()

    return render_template("found_items.html", items=items)


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    return redirect(url_for("home"))
# ---------------- START APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)