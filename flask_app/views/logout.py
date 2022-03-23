from flask import Blueprint

from ..controllers.LoginController import logout_account
logout  = Blueprint(
    'logout',
    __name__,
    template_folder = 'templates'
)

logout.route('/', methods=['GET','POST'])(logout_account)
