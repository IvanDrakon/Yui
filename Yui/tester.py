import os
import random
import numpy as np
import keras

from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.models import Model

root = "C:/Users/fabri/PetImages"
# train_split, val_split = 0.7, 0.15

# categories = [x[0] for x in os.walk(root) if x[0]][1:]
# print(categories)


def get_images(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x
#
#
# data = []
# for c, category in enumerate(categories):
#    images = [os.path.join(dp, f) for dp, dn, filenames in os.walk(category) for f in filenames if os.path.splitext(f)[1].lower() in ['.jpg', '.png', '.jpeg']]
#    for img_path in images:
#        try:
#            img, x = get_images(img_path)
#            data.append({'x':np.array(x[0]), 'y':c})
#        except:
#            print(img_path)
# num_classes = len(categories)
# #
# random.shuffle(data)
#
# idx_val = int (train_split * len(data))
# idx_test = int((train_split + val_split) * len(data))
# train = data[:idx_val]
# val = data[idx_val:idx_test]
# test = data[idx_test:]
# #
# x_train, y_train = np.array([t["x"] for t in train]), [t["y"] for t in train]
# x_val, y_val = np.array([t["x"] for t in val]), [t["y"] for t in val]
# x_test, y_test = np.array([t["x"] for t in test]), [t["y"] for t in test]
# print(y_test)
#
# x_train = x_train.astype('float32') / 255.
# x_val = x_val.astype('float32') / 255.
# x_test = x_test.astype('float32') / 255.
# #
# # convert labels to one-hot vectors
# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_val = keras.utils.to_categorical(y_val, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)

# vgg = keras.applications.VGG16(weights='imagenet', include_top=True)
# vgg.summary()
#
# # make a reference to VGG's input layer
# inp = vgg.input
#
# # make a new softmax layer with num_classes neurons
# new_classification_layer = Dense(num_classes, activation='softmax')
#
# # connect our new layer to the second to last layer in VGG, and make a reference to it
# out = new_classification_layer(vgg.layers[-2].output)
#
# # create a new network between inp and out
# model_new = Model(inp, out)
#
# # make all layers untrainable by freezing weights (except for last layer)
# for l, layer in enumerate(model_new.layers[:-1]):
#     layer.trainable = False
#
# # ensure the last layer is trainable/not frozen
# for l, layer in enumerate(model_new.layers[-1:]):
#     layer.trainable = True
#
# model_new.compile(loss='categorical_crossentropy',
#                   optimizer='adam',
#                   metrics=['accuracy'])
#
# model_new.summary()
model_new = keras.models.load_model('complete_saved_model/model.keras')

# loss, accuracy = model_new.evaluate(x_test, y_test, verbose=0)
# model_new.save('complete_saved_model/model.keras')

img, x = get_images(f"{root}/Dog/photo_2024-11-20_00-30-27.jpg")
probabilities = model_new.predict([x])
print(probabilities)

