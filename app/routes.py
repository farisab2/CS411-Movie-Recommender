""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper
import requests
import os
import urllib.request, json, urllib.parse
import sys
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


@app.route("/", methods=['GET', 'POST'])
def homepage():
    items = db_helper.movies()
    if request.method == 'POST':
        rating = request.form["rating"]
        movieid = request.form["movieID"]
        db_helper.insert_rating(rating, movieid)
        dict = []
        for item in items:
            url = "https://api.themoviedb.org/3/search/movie?api_key=b00e0a420be5aa6607c716ffa4320dce&query={}".format(urllib.parse.quote_plus(item["Title"]))
            response = urllib.request.urlopen(url)
            data = response.read()
            dict.append(json.loads(data))
        
        return render_template("index.html", items = items, movies = dict[0]["results"])
    else:
        dict = []
        for item in items:
            url = "https://api.themoviedb.org/3/search/movie?api_key=b00e0a420be5aa6607c716ffa4320dce&query={}".format(urllib.parse.quote_plus(item["Title"]))
            response = urllib.request.urlopen(url)
            data = response.read()
            dict.append(json.loads(data))
        
        return render_template("index.html", items = items, movies = dict[0]["results"])

@app.route("/<rating>")
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


@app.route("/mylist")
def mylistpage():
    items = db_helper.fetch_todo()
    return render_template("mylist.html", items = items)

@app.route("/search.html/")
def searchpage():
    return render_template("search.html")

@app.route("/recommendations.html/")
def recommendationspage():
    items = db_helper.fetchMovies()
    return render_template("recommendations.html", items=items)

@app.route("/recommendations2.html/")
def recommendationspage2():
    items = db_helper.fetchMoviesD()
    return render_template("recommendations2.html", items = items)

