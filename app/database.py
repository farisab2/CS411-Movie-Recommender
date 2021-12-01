from werkzeug.datastructures import ImmutableHeadersMixin
from app import db
import random

def my_movies() -> dict:

    conn = db.connect()
    query_results = conn.execute("SELECT movieID, title, score FROM Reviews natural join Movies WHERE userID = '001';").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        #print (result)
        item = {
            "id": result[0],
            "movie": result[1],
            "score": result[2]
        }
        todo_list.append(item)
    return todo_list


def update_rating(score: float, movieID: str) -> None:
    
    conn = db.connect()
    query = 'Update Reviews set score = "{}" where movieID = "{}" and userID = "001";'.format(score, movieID)
    conn.execute(query)
    conn.close()

def remove_review_by_id(movie_id: int) -> None:
    #remove entries based on task ID 
    conn = db.connect()
    query = 'Delete From Reviews where movieID = "{}" and userID = "001";'.format(movie_id)
    #print(query)
    conn.execute(query)
    conn.close()

def search_movies(searchTerm: str) -> dict:
    result = []
    conn = db.connect()
    searchTerm = searchTerm.replace("%20", " ")
    query = 'SELECT Title, releaseYear, numVotes, averageRating FROM Movies WHERE Title LIKE %s ORDER BY numVotes DESC LIMIT 15'
    args=['%' + searchTerm + '%']
    query_results =  conn.execute(query,args).fetchall()
    conn.close()
    for row in query_results:
        item = {
            "Title": row[0],
            "releaseYear": row[1],
            "numVotes": row[2],
            "averageRating": row[3]
        }
        result.append(item)
    return result


def movies() -> dict:
    result = []
    conn = db.connect()
    query = 'SELECT Title, releaseYear, numVotes, averageRating, movieID FROM Movies LIMIT 10'
    query_results = conn.execute(query).fetchall()
    conn.close()
    for row in query_results:
        item = {
            "Title": row[0],
            "releaseYear": row[1],
            "numVotes": row[2],
            "averageRating": row[3],
            "movieID": row[4]
        }
        result.append(item)
    random.shuffle(result)
    return result

def insert_rating(score: float, movieID: str) -> None:
    conn = db.connect()
    query = 'INSERT IGNORE INTO Reviews (userID, movieID, Score) VALUES ("001","{}","{}")'.format(str(movieID), score)
    conn.execute(query)
    query_results = conn.execute("Select Score FROM Reviews WHERE userID = 001;")
    query_results = [x for x in query_results]
    task_id = query_results[0]
    conn.close()
    return task_id
    
def fetchMovies()-> dict:
    result = []
    conn = db.connect()
    query = 'SELECT r.userID, r.movieID, m.Title, r.Score, m.releaseYear, m.averageRating, m.NumVotes FROM Reviews AS r JOIN Movies AS m ON r.movieID = m.movieID WHERE (r.UserID = "001" AND r.Score > 7) AND r.movieID IN (SELECT movieID FROM Reviews GROUP BY movieID HAVING AVG(Score) > 7) ORDER BY m.averageRating DESC'
    query_results = conn.execute(query).fetchall()
    conn.close()
    for row in query_results:
        item = {
            "userID": row[0],
            "movieID": row[1],
            "Title": row[2],
            "Score": row[3],
            "releaseYear": row[4],
            "averageRating": row[5],
            "NumVotes": row[6]
            
        }
        result.append(item)
    return result

def fetchMoviesD()-> dict:
    result = []
    conn = db.connect()
    query = 'SELECT * FROM Movies WHERE movieID IN (SELECT DISTINCT di.movieID FROM DirectorMapping di WHERE di.personID in (SELECT d.personID FROM DirectorMapping d INNER JOIN Reviews r ON d.movieID = r.movieID GROUP BY d.personID HAVING AVG(r.score) > 6)) ORDER BY averageRating DESC LIMIT 15'
    query_results = conn.execute(query).fetchall()
    conn.close()
    for row in query_results:
        item = {
            "movieID": row[0],
            "Title": row[1],
            "releaseYear": row[2],
            "averageRating": row[3],
            "NumVotes": row[4]
            
        }
        result.append(item)
    return result

def fetchMoviesDT()-> dict:
    result = []
    conn = db.connect()
    query = "SELECT * FROM Movies NATURAL JOIN DirectorMapping NATURAL JOIN (SELECT personID, SUM(score) AS totalPoints FROM Metrics GROUP BY personID) a NATURAL JOIN Directors WHERE movieID IN (SELECT movieID FROM DirectorMapping WHERE personID IN (SELECT di.personID FROM DirectorMapping di NATURAL JOIN Directors d JOIN Reviews r ON di.movieID = r.movieID WHERE d.tierStatus = 'Gold')) AND movieID NOT IN (SELECT movieID FROM Reviews WHERE userID = '001') ORDER BY a.totalPoints DESC LIMIT 15"
    query_results = conn.execute(query).fetchall()
    conn.close()
    for row in query_results:
        item = {
            "movieID": row[1],
            "Title": row[2],
            "releaseYear": row[3],
            "averageRating": row[4],
            "NumVotes": row[5],
            "firstName" : row[7],
            "lastName" : row[8]
            
        }
        result.append(item)
    return result
