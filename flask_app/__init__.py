
from flask import Flask, redirect,session,request,url_for,render_template,flash,jsonify
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread
import cv2
import random
import tensorflow as tf
from os import listdir
from sklearn.preprocessing import  LabelBinarizer
from keras.preprocessing.image import img_to_array
from sklearn.model_selection import train_test_split
from werkzeug.utils import secure_filename
from flask_migrate import Migrate

from .models.blogs import db

from .views.dashboard import dashboard
from .views.blogs import blogs
from .views.show import show
from .views.predictions import predictions
from .views.login import login
from .views.logout import logout
from .views.delete import delete

app = Flask(__name__)

 

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 

app.register_blueprint(dashboard, url_prefix='/')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(logout, url_prefix='/logout')
app.register_blueprint(blogs, url_prefix='/blogs')
app.register_blueprint(show, url_prefix='/show')
app.register_blueprint(predictions, url_prefix='/predictions')
app.register_blueprint(delete, url_prefix='/delete')

