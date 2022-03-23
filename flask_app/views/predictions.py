from flask import Blueprint

from ..controllers.PredictionController import index,upload
predictions  = Blueprint(
    'predictions',
    __name__,
    template_folder = 'templates'
)

predictions.route('/', methods=['GET'])(index)
predictions.route('/upload', methods=['POST'])(upload)