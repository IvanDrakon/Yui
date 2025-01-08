import numpy as np
import keras

from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input


def get_images(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x


def model_predict(path):
    model = keras.models.load_model('complete_saved_model/model.keras')
    img, x = get_images(path)
    probabilities = model.predict([x])
    cat = probabilities[0][0]
    dog = probabilities[0][1]
    return cat, dog
