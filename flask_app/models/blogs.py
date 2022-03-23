from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Blogs(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    blog_name = db.Column(db.String(250))
    blog_path = db.Column(db.String(250))
   
   
    def __init__(self,info):
        self.blog_name = info['blog_name']
        self.blog_path = info['blog_path']
