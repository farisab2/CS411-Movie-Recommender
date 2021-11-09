""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper
import requests
import os
import urllib.request, json
@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    #items = db_helper.top_rated_movies()
    # url = "https://api.themoviedb.org/3/discover/movie?api_key={}&page=3".format(os.environ.get("TMDB_API_KEY"))
    # response = urllib.request.urlopen(url)
    # data = response.read()
    # dict = json.loads(data)
    return render_template("index.html")

@app.route("/rate")
def ratings():
    # url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("TMDB_API_KEY"))
    # response = urllib.request.urlopen(url)
    # data = response.read()
    # dict = json.loads(data)

    return render_template("ratemovie.html");

@app.route("/search.html/<string:searchTerm>")
def search(searchTerm):
    #returns movies searched by User from User Table
    items = db_helper.search_movies(searchTerm)
    return render_template("search.html", items = items)


@app.route("/mylist.html/")
def mylistpage():
    return render_template("mylist.html")

@app.route("/search.html/")
def searchpage():
    return render_template("search.html")

@app.route("/recommendations.html/")
def recommendationspage():
    return render_template("recommendations.html")

