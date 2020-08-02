import tensorflow as tf
from tensorflow import keras
import pickle
import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob, os
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
image_directory = PROJECT_PATH + "/media/images/"

def test_data():
    fnames = os.listdir(image_directory)
    print(image_directory + fnames[0])
    test_img1 = cv2.imread(image_directory + fnames[0])
    plt.imshow(test_img1)
    test_img1 = cv2.resize(test_img1,(256,256))
    test_img1 = np.reshape(test_img1,[1,256,256,3])
    model_new = tf.keras.models.load_model(PROJECT_PATH + "/utils/potato.h5")

    with open(PROJECT_PATH + "/utils/label_transform.pkl", 'rb') as file:  
        label_binarizer = pickle.load(file)
   
    pr=model_new.predict(test_img1)
    output = label_binarizer.inverse_transform(pr)
    return output

