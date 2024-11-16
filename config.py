import os

class Config:
    SECRET_KEY = ('78900yt54zg@345679[]0',os.urandom(24))
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  
    MYSQL_DB = 'obituary_platform'
    MYSQL_CURSORCLASS = 'DictCursor'