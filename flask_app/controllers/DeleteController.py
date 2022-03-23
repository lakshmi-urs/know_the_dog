import imp
from flask_app import db
from ..models.blogs import Blogs
from ..models.posts import Posts
from flask import redirect,session,request,url_for,render_template,flash


def blog():
    blog_id = request.form['blog_id']
    db.session.query(Blogs).filter_by(id = int(blog_id)).delete()
    db.session.commit()
    db.session.close()
    flash("Blog deleted",'success')
    return redirect(url_for('blogs.blog'))

            
def post():
    post_id = request.form['post_id']
    db.session.query(Posts).filter_by(id = int(post_id)).delete()
    db.session.commit()
    db.session.close()
    flash("Post deleted",'success')
    return redirect(url_for('blogs.index'))