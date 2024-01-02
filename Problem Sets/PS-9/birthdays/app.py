import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
import secrets

# Configure application
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Validate the input data before adding to the database (optional)
        if not name or not month or not day:
            flash("Please provide all the required information.")
        else:
            # Insert the new entry into the database
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)
            flash("Birthday added successfully!")

        return redirect("/")

    else:
        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT name, month, day FROM birthdays")
        return render_template("index.html", birthdays=birthdays)


if __name__ == "__main__":
    app.run(debug=True)
