import cv2
import os

lego_brick_IDs = ["2357", "2420", "3003", "3004", "3005", "3022", "3039", "3659", "14719", "43857"]

def check_if_needed_type(filename):
    code = filename.split(' ')[0]
    if (code == lego_brick_IDs[0]
            or code == lego_brick_IDs[1]
            or code == lego_brick_IDs[2]
            or code == lego_brick_IDs[3]
            or code == lego_brick_IDs[4]
            or code == lego_brick_IDs[5]
            or code == lego_brick_IDs[6]
            or code == lego_brick_IDs[7]
            or code == lego_brick_IDs[8]
            or code == lego_brick_IDs[9]):
        return True
    return False


for filename in os.listdir("dataset"):
    img = cv2.imread(os.path.join("dataset", filename), cv2.IMREAD_COLOR)
    if check_if_needed_type(filename):
        cv2.imwrite("seperatedData/{}".format(filename), img)
