import cv2
from keras.models import load_model
from PIL import Image
import numpy as np


model = load_model('my_model.h5')
test = 'hello'
img = cv2.imread('C:\\Users\\HP\\Desktop\\finalyear\\pred\\pred8.jpg')


img = cv2.resize(img, (64, 64))  # Resize the image to (64, 64) pixels

# Preprocess the image data
img = img.astype('float32') / 255.0  # Normalize the pixel values
Input_Image = np.expand_dims(img, axis=0)  # Add a batch dimension

# Get the predicted probabilities for each class
result = model.predict(Input_Image)


# Get the predicted class label
predicted_class = np.argmax(result, axis=1)

print("Predicted class:", predicted_class)

if predicted_class==0:
    reso='nei'
elif predicted_class==1:
    reso='yei'

print(reso + "  nei = no , yei = yes")