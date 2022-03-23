import os
SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/blog_website'
#SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/blog_website'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False