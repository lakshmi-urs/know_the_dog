from flask import redirect,session,request,url_for,render_template,flash,jsonify
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
from os.path import join, dirname, realpath

UPLOAD_FOLDER = 'static/uploads'
absPath = dirname(realpath(__file__)) + '/../'
UPLOADS_PATH = join(absPath, 'static/uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def index():
       return render_template('predictions.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def upload():
    if 'files[]' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    files = request.files.getlist('files[]')


    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOADS_PATH, filename))

    #     
            dir = join(absPath, 'Dogs')
            root_dir = listdir(dir)
            image_list, label_list = [], []

            # Reading and converting image to numpy array
            for directory in root_dir:
                for files in listdir(f"{dir}/{directory}"):
                    image_path = f"{dir}/{directory}/{files}"
                    print(image_path)
                    image = cv2.imread(image_path)
                    image = img_to_array(image)
                    image_list.append(image)
                    label_list.append(directory)
            # print("FETCH COMPLETE TILL HERE")

    
            label_counts = pd.DataFrame(label_list).value_counts()
            label_counts

            num_classes = len(label_counts)
            num_classes

            image_list[0].shape

            label_list = np.array(label_list)

            x_train, x_test, y_train, y_test = train_test_split(image_list, label_list, test_size=0.2, random_state = 10)


            x_test = np.array(x_test, dtype=np.float16)/255.0

            x_test = x_test.reshape(-1,224, 224, 3)

    #         # Label binarizing
            lb = LabelBinarizer()
            y_train = lb.fit_transform(y_train)
            y_test = lb.fit_transform(y_test)

            model = tf.keras.models.load_model(join(absPath,"dog_species.h5"))
            print(model.summary())
    #         # Calculating test accuracy
            scores = model.evaluate(x_test, y_test)
            print(f"Test Accuracy: {scores[1]*100}")

    #         # Storing predictions
            y_pred = model.predict(x_test)



    #         # Finding max value from predition list and comaparing original value vs predicted
            labels = lb.classes_

            Result = labels[np.argmax(y_pred[4])]
            success = True
            print("Completed")

    resp = jsonify({
        'message' : 'Files successfully uploaded',
        'accuracy': str({scores[1]*100}),
        "Originally":str(labels[np.argmax(y_test[7])]),
        "Predicted":str(labels[np.argmax(y_pred[56])]),
        "Result": Result,
        "imageName": filename
        })
    resp.status_code = 200
    return resp
    # test_dir = "datasets/Test images/IDC/8863_idx5_x151_y1251_class0.png"

