from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
import numpy as np


def read_and_show_org_img(path):
    image = cv2.imread(path)
    cv2.imshow('uniform', image)
    res = cv2.waitKey(0)
    print('You pressed %d (0x%x), LSB: %d (%s)' % (res, res, res % 256,
                                                   repr(chr(res % 256)) if res % 256 < 128 else '?'))


def read_img(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resize_img = cv2.resize(image, (400, 770), interpolation=cv2.INTER_AREA)
    return resize_img


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color


def prep_image(raw_img):
    # modified_img = cv2.resize(raw_img, (900, 600), interpolation=cv2.INTER_AREA)
    modified_img = raw_img.reshape(raw_img.shape[0] * raw_img.shape[1], 3)
    return modified_img


def color_analysis(img):
    clf = KMeans(n_clusters=3)
    clf.fit(img)
    labels = clf.labels_
    labels = list(labels)
    centroid = clf.cluster_centers_
    percent = []
    hex_colors = []

    # Calculating percent each color
    for i in range(len(centroid)):
        j = labels.count(i)
        j = j / (len(labels))
        percent.append(j)
        hex_colors.append(rgb_to_hex(centroid[i]))

    return percent, centroid, hex_colors


def crop_and_analysis(path):
    # Crop image into 2 parts (shirt and trouser)
    img = read_img(path)
    shirt = img[150:350, :]
    trouser = img[400:550, 70:325]

    # Processing
    modified_shirt = prep_image(shirt)
    percent1, mat1, hex_colors1 = color_analysis(modified_shirt)
    modified_trouser = prep_image(trouser)
    percent2, mat2, hex_colors2 = color_analysis(modified_trouser)

    # Visualize
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.pie(percent1, colors=np.array(mat1 / 255), labels=hex_colors1)
    ax2.pie(percent2, colors=np.array(mat2 / 255), labels=hex_colors2)
    ax1.set_title("Shirt's color", fontsize=16, color='#525252')
    ax2.set_title("Trouser's color", fontsize=16, color='#525252')
    fig.suptitle("Uniform's color analysis", y=.1, fontsize=20, color='#525252')
    plt.show()
