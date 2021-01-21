import os
import string
import random
import PIL
import numpy as np
import tensorflow as tf
from tensorflow import keras

model = tf.keras.models.load_model('model/my_model.h5')

def make_prediction(data):
    img_height = 180
    img_width = 180
    img_url = data 
    img_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
    img_path = tf.keras.utils.get_file(img_name, origin=img_url)
    img = keras.preprocessing.image.load_img(
        img_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) 
    prediction = model.predict(img_array)
    score = tf.nn.softmax(prediction[0])
    class_names=['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
    return {'message':"most likely a {} with {:.2f} % confidence.".format(class_names[np.argmax(score)], 100 * np.max(score)),'img':data}
