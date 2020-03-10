from models.image import Image
import cv2


def load_from_path(path):
    img_arr = cv2.imread(path)
    return Image(img_arr)

