import sqlite3
import os
from openai import OpenAI

client = OpenAI(api_key="KEY")


from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "changes_this_later"


# ----------- DATABASE -----------
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT
        writing_profile TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()



# ----------- HOME ------------
@app.route("/")
def home():
    return render_template("home.html")



# ----------- REGISTER ----------
@app.route("/register", methods=["GET", "POST"])
def register():


    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]


        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()


        try:
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, hashed_password)
            )
            conn.commit()

        
        except:
            conn.close()
            return "Users already exists"
        

        conn.close()

        return redirect("/login")
    
    return render_template("register.html")




# -------------- LOGIN ---------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]


        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()


        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()


        conn.close()


        if user and check_password_hash(user[2], password):


            session["user_id"] = user[0]
            return redirect("/dashboard")
        
        
        return "Invalid login"
    

    return render_template("login.html")



# ----------- DASHBOARD -----------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "user_id" not in session:
        return redirect("/login")
    

    result = ""


    if request.method == "POST":


        text = request.form.get("text")


        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Rewrite the text to sound more natural and human while keeping the same meaning. Do not add new ideas."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        result = response.choices[0].message.content

    return render_template("dashboard.html", result=result)



# ------------ LOGOUT ---------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")



# --------- RUN (Render-ready) ------------
if __name__ == "__main__":


    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)    

