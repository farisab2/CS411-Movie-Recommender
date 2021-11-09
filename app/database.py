from werkzeug.datastructures import ImmutableHeadersMixin
from app import db

def fetch_todo() -> dict:

    todo_list = [
        {
            "id": 1,
            "task": "test1",
            "status": "Todo"
        },
        {
            "id": 2,
            "task": "test1",
            "status": "Todo"
        }
    ]
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
    query = 'SELECT Title, releaseYear, numVotes, averageRating FROM Movies WHERE Title LIKE %s LIMIT 15'
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
def top_rated_movies() -> dict:
    result = []
    conn = db.connect()
    query = 'SELECT Title, releaseYear, numVotes, averageRating FROM Movies ORDER BY averageRating DESC'
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