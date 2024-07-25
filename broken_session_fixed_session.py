#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)
app.secret_key = "11any random string"

@app.route("/")
def index():
  ## if the key "username" has a value in session
  if "username" in session and "age" in session:
     username = session["username"]
     age = session["age"]
     return f"Logged in as {username} <br> age is {age} <b><a href = '/logout'>click here to log out</a></b>"
  ## if the key "username" does not have a value in session
  return "You are not logged in & we don't know your age! <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route("/login", methods = ["GET", "POST"])
def login():
  ## if you sent us a POST because you clicked the login button
  if request.method == "POST":
     ## request.form["xyzkey"]: use indexing if you know the key exists
     ## request.form.get("xyzkey"): use get if the key might not exist
     session["username"] = request.form.get("username")
     session["age"] = request.form.get("age")
     return redirect(url_for("index"))

 ## return this HTML data if you send us a GET
  return """
   <form action = "/login" method = "post">
      <p><input type = text name = username></p>
      <p><input type = text name = age></p>
      <p><input type = submit value = Login></p>
   </form>"""

@app.route("/logout")
def logout():
  # remove the username from the session if it is there
  session.pop("username", None)
  session.pop("age", None)
  return redirect(url_for("index"))
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224)



