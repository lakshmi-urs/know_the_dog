from flask import Blueprint

from ..controllers.ShowController import index,post
show  = Blueprint(
    'show',
    __name__,
    template_folder = 'templates'
)

show.route('/<blog_path>', methods=['GET'])(index)
show.route('/<blog_path>/<post_link>', methods=['GET'])(post)