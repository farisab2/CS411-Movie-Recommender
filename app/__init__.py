import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader

app = Flask(__name__)

def init_connection_engine():
    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    ) # pool is connection to GCP

    return pool

db = init_connection_engine()

#testing connection to GCP
conn = db.connect()
results = conn.execute("SELECT * FROM Genres;").fetchall()
print([x for x in results])
conn.close()

#remember to run (on Powershell), not in order:
# $env:FLASK_APP = "app"
# $env:FLASK_DEBUG = 1
# python -m flask run
 
from app import routes