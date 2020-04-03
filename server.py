from flask import Flask, render_template, request, session, redirect, url_for, Markup
from sqlalchemy import exc,func
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint
import datetime

app = Flask(__name__)

def get_final_score(data):

    try:
        fname = data['fname']
        lname = data['lname']
        age = data['age']
        gender = data['gender']
    except:
        return -1

    score = 0
    for k,v in data.items():
        if k not in ['fname', 'lname', 'age', 'gender', 'contact-date', 'conditions-other', 'conditions']:
            try:
                score += float(v)
            except:
                pass

    try:
        format_str = '%Y-%m-%d'
        date = datetime.datetime.strptime(data['contact-date'], format_str)
        days = (datetime.datetime.today() - date).days

        if days < 14:
            score += 3
        elif days >= 21:
            score -= 3
    except:
        pass

    try:
        for val in data.getlist('condititions'):
            score += float(val)
    except:
        pass

    try:
        if data['conditions-other']:
            score += 1
    except:
        pass

    return score

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/form", methods=['GET'])
def form():
    return render_template("symptom-form.html")

@app.route("/form_submit", methods=['POST'])
def form_submit():
    try:
        data = request.form
        score = get_final_score(data)

        if score < 0:
            return render_template('error.html', data={'callback': 'form', 'message': 'The name / age / gender fields are incomplete. Please fill these fields  '})

        if score < 10:
            color = 'bg-success'
            content = 'No risk'
        elif 10 <= score < 17:
            color = 'bg-warning'
            content = 'Moderate risk'
        elif 17 <= score < 21:
            color = 'bg-warning'
            content = 'Consult a nearby doctor'
        else:
            color = 'bg-danger'
            content = 'High risk'

        result_data = {
            'value': 2*(int(score)),
            'content': content,
            'color': color,
        }
    except:
        return render_template('error.html', data={'callback': 'form', 'message': 'An unknown error occured'})

    print(result_data)
    return render_template('results.html', data=result_data)

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
