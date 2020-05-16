import cv2
import numpy as np
import os


def resize_images(src, destination, grayscale):
    for filename in os.listdir(src):
        if grayscale:
            image = cv2.imread(os.path.join(src, filename), cv2.IMREAD_GRAYSCALE)
            img = np.dstack((image, image, image))
        else:
            img = cv2.imread(os.path.join(src, filename), cv2.IMREAD_COLOR)

        filename_without_extension = filename.split(".")
        resized = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        cv2.imwrite("{}/{}.jpg".format(destination, filename_without_extension[0]), resized)
        print("Reszied: {}".format(filename))


resize_images("rwTestData", "rwResizedGrayscale", True)
