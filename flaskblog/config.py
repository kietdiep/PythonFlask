import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    DEBUG = True
    TESTING = False 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USE_SSL = False
    #MAIL_DEBUG = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL_USER') 
    MAIL_MAX_EMAILS = None
    #MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False 