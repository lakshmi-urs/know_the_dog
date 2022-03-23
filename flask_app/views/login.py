from flask import Blueprint

from ..controllers.LoginController import index
login  = Blueprint(
    'login',
    __name__,
    template_folder = 'templates'
)

login.route('/', methods=['GET','POST'])(index)
