import os

DEBUG =  True
SECRET_KEY = os.urandom(24)
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'question'
USENAME = 'root'
PASSWORD = 'puhao'
DB_URI = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(USENAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
