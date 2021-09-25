from utility import utils
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    utils.crop_and_analysis('images/student5.jpg')
    utils.read_and_show_org_img('images/student5.jpg')
