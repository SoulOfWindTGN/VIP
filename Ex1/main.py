from glob import glob
import cv2 as cv
from utility import utils


if __name__ == '__main__':
    video_paths = glob('Video/*')  # Lấy đường dẫn toàn bộ video trong thư mục Video
    image_paths = "Image"  # Thư mục lưu ảnh

    # Trích frame từ video
    for path in video_paths:
        utils.save_frame(path, image_paths, start=0, step=500)

    # Chuyển ảnh RGB về grayscale
    img = cv.imread("Lenna.png")
    gray = utils.convert_grayscale(img)
    cv.imwrite("Lenna_gray.png", gray)
