from flask import Blueprint

from ..controllers.DeleteController import blog,post

delete  = Blueprint(
    'delete',
    __name__,
    template_folder = 'templates'
)

delete.route('/blog', methods=['POST'])(blog)
delete.route('/post', methods=['POST'])(post)