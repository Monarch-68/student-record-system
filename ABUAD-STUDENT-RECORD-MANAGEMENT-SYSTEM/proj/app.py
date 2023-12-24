import numpy as np 
import cv2
import os
from keras.models import load_model
import tensorflow as tf
from PIL import Image
from keras.preprocessing import image
from flask import Flask,request,render_template

app= Flask(__name__)


model= ('my_model.keras')
print("Model loaded succesfully.check https://127.0.0.1:5000/")


def get_classname(classNo):
    if classNo==0:
        return'no brain tumor'
    elif classNo==1:
        return 'brain tumor detected'
    

def getResult(img):
    Image=cv2.imread(img)
    Image= Image.fromarray(image,"RGB")
    Image= Image.resize((64,64))
    Image=np.array(Image)
    Input_Image = np.expand_dims(img, axis=0) 
    result = model.predict(Input_Image)



