import cv2
from matplotlib import pyplot as plt

#  Dictionary for analysis hsv image
h_dictionary = {'0': 'Red', '1': 'Yellow - Orange', '2': 'Green', '3': 'Blue', '4': 'Pink'}
s_v_dictionary = {'0': 'Low', '1': 'Medium', '2': 'High'}


def dominant_cal(hist_h, hist_s, hist_v):
    color = []
    saturation = []
    value = []

    # calculate color
    color.append(sum(hist_h[0:11])[0] + sum(hist_h[170:181])[0])  # Red
    color.append(sum(hist_h[11:31])[0])  # Yellow - Orange
    color.append(sum(hist_h[31:81])[0])  # Green
    color.append(sum(hist_h[81:141])[0])  # Blue
    color.append(sum(hist_h[141:170])[0])  # Pink

    # calculate saturation
    saturation.append(sum(hist_s[0:86])[0])  # low
    saturation.append(sum(hist_s[86:170])[0])  # medium
    saturation.append(sum(hist_s[170:256])[0])  # high

    # calculate bright
    value.append(sum(hist_v[0:86])[0])  # low
    value.append(sum(hist_v[86:170])[0])  # medium
    value.append(sum(hist_v[170:256])[0])  # high

    return color, saturation, value

def analysis(img, title = ""):
    # cal hist
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
    hist_h = cv2.calcHist([h], [0], None, [256], [0, 256])
    hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
    hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])

    # plot
    plt.plot(hist_h, color='r', label="h")
    plt.plot(hist_s, color='g', label="s")
    plt.plot(hist_v, color='b', label="v")
    plt.legend()
    plt.title(title)
    plt.show()

    # color analysis
    color, saturation, value = dominant_cal(hist_h, hist_s, hist_v)
    max_h = color.index(max(color))
    max_s = saturation.index(max(saturation))
    max_v = value.index(max(value))
    print('Màu chủ đạo:', h_dictionary[str(max_h)])
    print('Độ bão hòa:', s_v_dictionary[str(max_s)])
    print('Độ sáng:', s_v_dictionary[str(max_v)])


if __name__ == '__main__':
    img = cv2.imread('images/worker2.jpg')
    img = cv2.resize(img, (400, 770), interpolation=cv2.INTER_AREA)
    shirt = img[150:350, :]
    trouser = img[400:550, 70:325]
    print("Thông tin màu sắc của áo")
    analysis(shirt, 'shirt')
    print("Thông tin màu sắc của quần")
    analysis(trouser, 'trouser')
    cv2.imshow('shirt', shirt)
    cv2.imshow('trouser', trouser)
    cv2.waitKey(0)
