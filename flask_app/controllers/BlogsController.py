# import hashlib
# For Hashing Password

from flask_app import db
import json
# from ..models.pypies import Pypies 
from ..models.blogs import Blogs
from ..models.posts import Posts
# from ..models.votes import Votes

from flask import redirect,session,request,url_for,render_template,flash,jsonify

def index():
        blogs =[]
        results = db.session.query(Blogs).filter_by().all()
        db.session.close()
        for res in results:
                resPosts = db.session.query(Posts).filter_by(blog_id = res.id).all()
                db.session.commit()
                db.session.close()
                total_posts = 0

                for respost in resPosts:
                        total_posts +=1

                res.total_posts = total_posts
                blogs.append(res)

        return render_template('blogs.html',blogs=blogs)


def add():
        if 'Email' in session:
                return render_template('add_blog.html')
        else:
                return redirect(url_for("blogs.index"))

def edit():
        if 'Email' in session:
                return render_template('edit.html')
        else:
                return redirect(url_for("blogs.index"))

def blog():

        if 'Email' in session:
                if request.method == 'POST':
                        if request.form['action'] == 'update_blog':
                                blog_id = request.form['blog_id']
                                blog_name = request.form['blog_name']
                                blog_path = blog_name.replace(" ","_")
                                blog_check = db.session.query(Blogs).filter_by(blog_path = blog_path).first()
                                if  blog_check is None:
                                        blogData = db.session.query(Blogs).filter_by(id = blog_id).first()
                                        blogData.blog_name = blog_name
                                        blogData.blog_path = blog_path
                                        db.session.commit()
                                
                                        db.session.close()
                                        flash("Blog Updated Successfully","success")
                                        return redirect(url_for('blogs.blog'))
                                else:
                                        flash("Blog with that title already exists","danger")
                                        return redirect(url_for('blogs.blog'))
                else:

                        blogs =[]
                        results = db.session.query(Blogs).filter_by().all()
                        db.session.close()
                        for res in results:
                                resPosts = db.session.query(Posts).filter_by(blog_id = res.id).all()
                                db.session.commit()
                                db.session.close()
                                total_posts = 0

                                for respost in resPosts:
                                        total_posts +=1

                                res.total_posts = total_posts
                                blogs.append(res)

                        return render_template('blog.html',blogs=blogs)
        else:
                return redirect(url_for("blogs.index"))

def create():
        if 'Email' in session:
                if request.method=='POST':
                        if request.form['action'] == 'create_blog':
                                blog_name = request.form['blog_name']
                                blog_path = blog_name.replace(" ","_")
                                blog_path = blog_path.replace("?","_")
                                blog_path = blog_path.replace("@","_")
                                blog_check = db.session.query(Blogs).filter_by(blog_path = blog_path).first()
                                if blog_check is None:
                                        Info = {
                                                "blog_name": blog_name,
                                                "blog_path": blog_path
                                        }
                                        blog_add = Blogs(Info)
                                        db.session.add(blog_add)
                                        db.session.commit()
                                        db.session.close()
                                        flash("Blog Created Successfully","success")
                                        return redirect(url_for('blogs.existing'))
                                else:
                                        flash("Blog with that title already exists","danger")
                                        return redirect(url_for('blogs.create'))
                        
                        else:
                                flash("Blog with that title already exists","danger")
                                return redirect(url_for('dashboard.index'))
                else:
                        return render_template('create.html')

        else:
                return redirect(url_for("blogs.index"))

def existing():
        if 'Email' in session:
                if request.method == 'POST':
                        if request.form['action'] == 'create_post':
                                post_title = request.form['post_title']
                                post_description = request.form['post_description']
                                post_link = post_title.replace(" ","_")
                                post_link = post_link.replace("@","_")
                                post_link = post_link.replace("#","_")
                                post_link = post_link.replace("?","_")
                                blog_id = request.form['blog_id']
                                post_check = db.session.query(Posts).filter_by(post_link = post_link).first()
                                if post_check is None:
                                        Info = {
                                                "post_title": post_title,
                                                "post_description": post_description,
                                                "post_link": post_link,
                                                "blog_id": blog_id
                                        }
                                        post_add = Posts(Info)
                                        db.session.add(post_add)
                                        db.session.commit()
                                        db.session.close()
                                        flash("Post Created Successfully","success")
                                        return redirect(url_for('blogs.index'))
                                else:
                                        flash("Blog with that title already exists","danger")
                                        return redirect(url_for('blogs.create'))
                        elif request.form['action'] == 'update_post':
                                post_title = request.form['post_title']
                                post_description = request.form['post_description']
                                post_link = post_title.replace(" ","_")
                                post_link = post_link.replace("@","_")
                                post_link = post_link.replace("#","_")
                                post_link = post_link.replace("?","_")
                                post_id = int(request.form['post_id'])
                                post_check = db.session.query(Posts).filter(Posts.post_link == post_link, Posts.id != post_id).first()
                                db.session.close()
                                if post_check is None:
                                        postUpdate = db.session.query(Posts).filter_by(id = post_id).first()
                                        postUpdate.post_title = post_title
                                        postUpdate.post_description = post_description
                                        postUpdate.post_link = post_link
                                        db.session.commit()
                                        db.session.close()
                                        flash("Post Updated Successfully","success")
                                        return redirect(url_for('blogs.index'))
                                else:
                                        flash("Post with that title already exists","danger")
                                        return redirect(url_for('blogs.create'))
                        else:
                                flash("Post with that title already exists","danger")
                                return redirect(url_for('dashboard.index'))
                        
                else:
                        blogs = []
                        results  = db.session.query(Blogs).filter_by().all()
                        for res in results:
                                blogs.append(res)
                        return render_template('existing.html',blogs=blogs)

        else:
                return redirect(url_for("blogs.index"))

def edit_blog(blog_id):
        if 'Email' in session:
                blog = db.session.query(Blogs).filter_by(id=int(blog_id)).first()
                db.session.close()
                return render_template("update_blog.html",blog = blog )

        else:
                return redirect(url_for("blogs.index"))
def view_posts_to_edit(blog_id):
        if 'Email' in session:
                posts = []
                result_data = db.session.query(Posts).filter_by(blog_id=int(blog_id)).all()
                db.session.close()
                for res in result_data:
                        posts.append(res)


                print(posts)
                return render_template("view_posts_to_edit.html",posts=posts,blog_id=blog_id)

        else:
                return redirect(url_for("blogs.index"))
def post():
        if 'Email' in session:

                blogs = []
                results  = db.session.query(Blogs).filter_by().all()
                db.session.close()
                for res in results:
                                resPosts = db.session.query(Posts).filter_by(blog_id = res.id).all()
                                db.session.close()
                                total_posts = 0

                                for respost in resPosts:
                                        total_posts +=1

                                res.total_posts = total_posts
                                blogs.append(res)
                return render_template('blog_for_post.html',blogs=blogs)

        else:
                return redirect(url_for("blogs.index"))

def edit_post(blog_id,post_id):
        if 'Email' in session:
                post = db.session.query(Posts).filter_by(id=int(post_id)).first()
                db.session.close()
                return render_template("update_post.html",post = post,blog_id=blog_id )

        else:
                return redirect(url_for("blogs.index"))