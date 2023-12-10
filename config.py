import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Sill have no clue what im doing'
    SQLALCHEMY_DATABASE_URI = "postgresql://jplzcyrq:5Mae4oXflyfk6-cYDOv1oM0lVdQyDQsf@bubble.db.elephantsql.com/jplzcyrq"
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    print(SQLALCHEMY_DATABASE_URI)