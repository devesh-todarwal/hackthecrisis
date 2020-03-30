from flask import Flask, render_template, request, session, redirect, url_for, Markup
from sqlalchemy import exc,func
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
"""
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://manan:psql@localhost/manan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()

sample
@app.route("/", methods=['GET'])
def index():
    try:
        uname, logged_in = session['user']
        if logged_in:
            return redirect(url_for("home"))
        else:
            return render_template("index.html")
    except KeyError:
        return render_template("index.html")
"""

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/form", methods=['GET'])
def form():
    return render_template("symptom-form.html")

@app.route("/page1", methods=['GET'])
def page1():
    return render_template("page1.html")

@app.route("/page2", methods=['GET'])
def page2():
    return render_template("page2.html")

@app.route("/page3", methods=['GET'])
def page3():
    return render_template("page3.html")

if __name__ == '__main__':
    app.run(debug=True,port=5000)
