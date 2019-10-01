import os
from app import app
from flask import render_template, request, redirect


events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event":"Summer vacation", "date":"2019-12-03"}
    ]


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://chairman:helloman@cluster0-ae6gd.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    events = mongo.db.Events
    if dict(request.form):
        userdata = dict(request.form)
        event_date= userdata["date of event:"]
        event_name = userdata["name of event:"]
        events.insert({"event_name":event_name,"event_date":event_date})

    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    test = mongo.db.test
    test.insert({'name':'last day of school'})
    # connect to the database

    # insert new data

    # return a message to the user
    return "added data to database"

@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/results', methods = ["GET","POST"])
def results():
    userdata = dict(request.form)
    #return (userdata)
    event_date= userdata["date of event:"]
    event_name = userdata["name of event:"]
    events = mongo.db.Events
    events.insert({"event_name":event_name,"event_date":event_date})



    return ("this is results page")
