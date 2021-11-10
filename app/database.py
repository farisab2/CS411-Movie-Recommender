from werkzeug.datastructures import ImmutableHeadersMixin
from app import db
import random

def fetch_todo() -> dict:

    conn = db.connect()
    query_results = conn.execute("SELECT * FROM Movies;").fetchall()
    conn.close()
    todo_list = []
    x = 0
    for result in query_results:
        print (result)
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
        if (x > 10):
            break
        x = x + 1
    return todo_list

def fetch_todo1() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("SELECT * FROM Movies;").fetchall()
    conn.close()
    todo_list = []
    x = 0
    for result in query_results:
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
        if (x > 10):
            break
        x = x + 1

    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`
    Args:
        task_id (int): Targeted task_id
        text (str): Updated description
    Returns:
        None
    

    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()
    """
    pass


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`
    Args:
        task_id (int): Targeted task_id
        text (str): Updated status
    Returns:
        None
    

    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close() """
    pass


def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.
    Args:
        text (str): Task description
    Returns: The task ID for the inserted entry
    

    conn = db.connect()
    query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id """
    pass
    return 1


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID 
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close() """
    pass

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
    """
    result = [
        {
            "Title": "Shrek",
            "yearReleased": "2001",
            "numVotes": 1010231,
            "averageRating": 9.4
        },
        {
            "Title": "Wall-E",
            "yearReleased": "2008",
            "numVotes": 93854,
            "averageRating": 7.9
        }
    ]"""
    return result


def movies() -> dict:
    result = []
    conn = db.connect()
    query = 'SELECT Title, releaseYear, numVotes, averageRating FROM Movies LIMIT 10'
    query_results = conn.execute(query).fetchall()
    conn.close()
    for row in query_results:
        item = {
            "Title": row[0],
            "releaseYear": row[1],
            "numVotes": row[2],
            "averageRating": row[3]
        }
        result.append(item)
    random.shuffle(result)
    return result

def insert_rating(userID: str, score: float, movieID: str):
    conn = db.connect()
    query = 'INSERT INTO Reviews (userID, movieID, Score) VALUES ({}.{}.{}) ON DUPLICATE KEY UPDATE userID = {}'.format(userID, movieID, score, userID)

    result.append(item)
    
def fetchMovies()-> dict:
    result = []
    conn = db.connect()
    query = 'SELECT r.userID, r.movieID, m.Title, r.Score, m.releaseYear, m.averageRating, m.NumVotes FROM Reviews AS r INNER JOIN Movies AS m ON r.movieID = m.movieID WHERE (r.UserID = "001" AND r.Score > 7) AND r.movieID IN (SELECT movieID FROM Reviews GROUP BY movieID HAVING AVG(Score) > 7) ORDER BY m.averageRating DESC'
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
    query = 'SELECT * FROM Movies WHERE movieID IN (SELECT DISTINCT di.movieID FROM DirectorMapping di WHERE di.Director in (SELECT d.Director FROM DirectorMapping d INNER JOIN Reviews r ON d.movieID = r.movieID GROUP BY d.Director HAVING AVG(r.score) > 6)) ORDER BY averageRating DESC'
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
