import cv2
import numpy as np
import os
import h5py
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def save_h5_data(filename, x_test, y_test):
    with h5py.File(filename, "w") as out:
        out.create_dataset("x_test", data=x_test, compression="gzip", compression_opts=8)
        out.create_dataset("y_test", data=y_test, compression="gzip", compression_opts=8)
    print("H5 file saved!")


def init_data_generator():
    data_generator = ImageDataGenerator(
        rescale=1. / 255,
        width_shift_range=[-30, 30],
        height_shift_range=[-30, 30],
        horizontal_flip=True,
        vertical_flip=True,
        rotation_range=360,
        zoom_range=[1.5, 1.5])

    return data_generator


def load_and_save_data(src, save_name):
    images = np.empty((1000, 224, 224, 3))
    labels = np.empty(1000)

    data_generator = init_data_generator()

    for (i, filename) in enumerate(os.listdir(src)):
        image = cv2.imread(os.path.join(src, filename), cv2.IMREAD_COLOR)
        train_data = data_generator.flow(np.reshape(image, (1, 224, 224, 3)), batch_size=1)
        for j in range(10):
            img = train_data.next()
            img = np.reshape(img, (224, 224, 3))
            images[i * 10 + j] = img
            labels[i * 10 + j] = filename[0]

    np.random.seed(77)
    np.random.shuffle(images)
    np.random.seed(77)
    np.random.shuffle(labels)

    print("Loaded images!")
    save_h5_data(save_name, images, labels)


load_and_save_data("rwResizedColor", "legobricks_rwColorAug.h5")
# load_and_save_data("rwResizedGrayscale", "legobricks_rwGrayAug.h5")
