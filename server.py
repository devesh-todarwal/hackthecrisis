from flask import Flask, render_template, request, session, redirect, url_for, Markup
from sqlalchemy import exc,func
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint
import datetime
import random

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

@app.route("/map", methods=['GET'])
def map():
    return render_template("map.html")

@app.route("/bus", methods=['GET'])
def bus():
    nodes = ['Kalyan-Dombivali', 'Navi Mumbai', 'Thane', 'Thane', 'Ulhasnagar', 'Vasai-Virar', 'Palghar', 'Mira-Bhayandar']
    return render_template("bus.html",nodes=nodes)

@app.route("/bus_submit", methods=['POST'])
def bus_submit():
    try:
        src = int(request.form['src'])
        dst = int(request.form['dst'])
        print(src,dst)
        path_len = random.randint(3,5)
        if src == dst:
            path_len = 0
        chosen = -1
        path = []
        nodes = [n for n in range(7) if n not in [src,dst]]
        for j in range(path_len):
            if chosen != -1:
                try:
                    nodes.remove(chosen)
                except:
                    pass
            chosen = random.choice(nodes)
            path.append(chosen)
        path = [src] + path + [dst]
        path_edges = [[path[i-1],path[i]] for i in range(1,len(path))]

        rest = list(range(7))
        try:
            rest.remove(src)
        except:
            pass
        try:
            rest.remove(dst)
        except:
            pass
        edges = []
        for i in rest:
            for j in rest:
                if i!=j:
                    edges.append([i,j])

        data = {
            'src': src,
            'dst': dst,
            'rest': rest,
            'inv': ['Kalyan-Dombivali', 'Navi Mumbai', 'Thane', 'Thane', 'Ulhasnagar', 'Vasai-Virar', 'Palghar', 'Mira-Bhayandar'],
            'edges': edges,
            'path-edges': path_edges,
        }
        return render_template("bus_submit.html",data=data)
    except:
        return render_template('error.html', data={'callback': 'bus', 'message': 'An unknown error occured'})


if __name__ == '__main__':
    app.run(debug=True,port=5000)
