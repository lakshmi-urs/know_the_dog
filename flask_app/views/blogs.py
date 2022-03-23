from flask import Blueprint

from ..controllers.BlogsController import index,add,create,existing,edit,blog,post,edit_blog,view_posts_to_edit,edit_post
blogs  = Blueprint(
    'blogs',
    __name__,
    template_folder = 'templates'
)

blogs.route('/', methods=['GET'])(index)
blogs.route('/add', methods=['GET'])(add)
blogs.route('/add/create', methods=['GET','POST'])(create)
blogs.route('/add/existing', methods=['GET','POST'])(existing)
blogs.route('/edit', methods=['GET'])(edit)
blogs.route('/edit/blog', methods=['GET','POST'])(blog)

blogs.route('/edit/post', methods=['GET','POST'])(post)

blogs.route('/edit/blog/<blog_id>', methods=['GET'])(edit_blog)
blogs.route('/edit/blog/<blog_id>/posts', methods=['GET'])(view_posts_to_edit)
blogs.route('/edit/blog/<blog_id>/posts/<post_id>', methods=['GET'])(edit_post)