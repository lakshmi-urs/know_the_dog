from flask import Blueprint

from ..controllers.DashboardController import index,dashboard_page
# ,delete

dashboard  = Blueprint(
    'dashboard',
    __name__,
    template_folder = 'templates'
)

dashboard.route('/', methods=['GET','POST'])(index)
dashboard.route('/dashboard', methods=['GET','POST'])(dashboard_page)
# dashboard.route('/delete', methods=['GET','POST'])(delete)