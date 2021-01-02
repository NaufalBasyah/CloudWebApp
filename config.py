import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'halo-sayang'
    host=os.environ.get('DB_HOST') or 'catalogue-db-246.cwzhix86ir4v.us-east-1.rds.amazonaws.com'
    username=os.environ.get('DB_USERNAME') or 'psecloud5'
    password=os.environ.get('DB_PASSWORD') or 'crimson7'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://' + username + ':' + password + '@' + host + '/cloud'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
