import cv2
import numpy as np
import os
import h5py
import math


lego_brick_IDs = ["2357", "2420", "3003", "3004", "3005", "3022", "3039", "3659", "14719", "43857"]
folder_name = "withoutBottomData"


def number_of_images():
    count: int = 0
    for _ in os.listdir("withoutBottomData"):
        count += 1
    return count


def save_h5_data(x_train, y_train, x_val, y_val, x_test, y_test, ):
    file_name = 'legobricks_data_withoutBot.h5'
    with h5py.File(file_name, "w") as out:
        out.create_dataset("x_train", data=x_train, compression="gzip", compression_opts=8)
        out.create_dataset("y_train", data=y_train, compression="gzip", compression_opts=8)
        out.create_dataset("x_test", data=x_test, compression="gzip", compression_opts=8)
        out.create_dataset("y_test", data=y_test, compression="gzip", compression_opts=8)
        out.create_dataset("x_val", data=x_val, compression="gzip", compression_opts=8)
        out.create_dataset("y_val", data=y_val, compression="gzip", compression_opts=8)
    print("H5 file saved!")


def get_label(filename):
    code = filename.split(' ')[0]
    if code == lego_brick_IDs[0]:  # brick corner 1x2x2
        return 0
    elif code == lego_brick_IDs[1]:  # plate corner 2x2
        return 1
    elif code == lego_brick_IDs[2]:  # brick 2x2
        return 2
    elif code == lego_brick_IDs[3]:  # brick 1x2
        return 3
    elif code == lego_brick_IDs[4]:  # brick 1x1
        return 4
    elif code == lego_brick_IDs[5]:  # plate 2x2
        return 5
    elif code == lego_brick_IDs[6]:  # roof tile 2x2
        return 6
    elif code == lego_brick_IDs[7]:  # brick bow 1x4
        return 7
    elif code == lego_brick_IDs[8]:  # flat tile corner 2x2
        return 8
    elif code == lego_brick_IDs[9]:  # beam 1x2
        return 9


def split_data(images, labels):
    np.random.seed(5)
    np.random.shuffle(images)
    np.random.seed(5)
    np.random.shuffle(labels)

    train_number = math.floor(len(labels) * 0.65)
    val_number = math.floor(len(labels) * 0.2)
    test_number = train_number + val_number

    x_train = images[0:train_number]
    y_train = labels[0:train_number]  # 65% of data
    x_val = images[train_number:test_number]
    y_val = labels[train_number:test_number]  # 20% of data
    x_test = images[test_number:]
    y_test = labels[test_number:]  # 15% of data

    print("Images split in train, val and test!")
    return x_train, y_train, x_val, y_val, x_test, y_test


def load_images(folder_name):
    num_of_img = number_of_images()
    images = np.empty((num_of_img, 224, 224, 3))
    labels = np.empty(num_of_img)

    for (i, file_name) in enumerate(os.listdir(folder_name)):
        images[i] = cv2.imread(os.path.join(folder_name, file_name), cv2.IMREAD_COLOR)
        labels[i] = get_label(file_name)

    print("Loaded images!")
    return images, labels


images, labels = load_images(folder_name)
x_train, y_train, x_val, y_val, x_test, y_test = split_data(images, labels)
save_h5_data(x_train, y_train, x_val, y_val, x_test, y_test)
