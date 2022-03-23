import imp
from flask_app import db
from ..models.blogs import Blogs
from ..models.posts import Posts
from flask import redirect,session,request,url_for,render_template,flash


def index(blog_path):
    print(blog_path)
    result = db.session.query(Blogs).filter_by(blog_path = blog_path).first()
    print(result)
    print(result.id)
    blog = result
    db.session.close()
    posts = []
    if not(result is None):
        resPosts = db.session.query(Posts).filter_by(blog_id = result.id).all()
        for res in resPosts:
            posts.append(res)
        return render_template("show.html",blog= blog,posts=posts)

    else:
        flash("That blog doesn't exist",'danger')
        return redirect(url_for('blogs.index'))

            
def post(blog_path,post_link):
    result = db.session.query(Blogs).filter_by(blog_path = blog_path).first()
    print(result)
    db.session.close()
    blog = result
    posts = []
    if not (result is None):
        resPosts = db.session.query(Posts).filter_by(post_link = post_link).first()
        posts = resPosts
        return render_template("show_post.html",blog= blog,posts=posts)

    else:
        flash("That post doesn't exist",'danger')
        return redirect(url_for('blogs.index'))

