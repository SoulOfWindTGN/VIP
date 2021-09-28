import os
import numpy as np
import cv2 as cv


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")


def convert_grayscale(img):
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])


def save_frame(video_path, save_dir, start=0, step=0):
    name = video_path.split("\\")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.release()
            break

        if idx >= start and idx % step == 0:
            cv.imwrite(f"{save_path}/{idx}.jpg", frame)

        idx += 1


