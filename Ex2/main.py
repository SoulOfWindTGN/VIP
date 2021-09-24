from utility import utils
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    utils.crop_and_analysis('images/student2.jpg')
    utils.read_and_show_org_img('images/student2.jpg')
