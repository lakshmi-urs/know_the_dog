from datetime import datetime
from flask_app import db

class Posts(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    post_title = db.Column(db.String(255))
    post_description = db.Column(db.Text)
    post_date = db.Column(db.DateTime())
    post_link = db.Column(db.String(250))
    blog_id = db.Column(db.Integer)
   
    def __init__(self,info):

        self.post_title = info['post_title']
        self.post_description = info['post_description']
        self.post_date = datetime.today()
        self.post_link = info['post_link']
        self.blog_id = info['blog_id']
    
