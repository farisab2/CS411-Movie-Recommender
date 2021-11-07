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
    pass


def update_status_entry(task_id: int, text: str) -> None:
    pass


def insert_new_task(text: str) ->  int:
    pass
    return 1


def remove_task_by_id(task_id: int) -> None:
    pass

def search_movies() -> dict:
    """ result = []
    conn = db.connect()
    query =  conn.execute("SQL stuff").fetchall()
    conn.close()
    for row in query:
        item = {

        }
        result.append(item) """

    result = [
        {
            "Title": "Shrek",
            "yearReleased": "2001",
            "Director": "Me",
            "Votes": 1010231,
            "Score": 9.4
        },
        {
            "Title": "Wall-E",
            "yearReleased": "2008",
            "Director": "You",
            "Votes": 93854,
            "Score": 7.9
        }
    ]
    return result