from src.models.image import Image
import cv2
from uuid import uuid4
from src.telegram_api.config import TMP_PATH


def load_from_path(path):
    img_arr = cv2.imread(path)
    return Image(img_arr)


def generate_file_name():
    return '{}.jpg'.format(uuid4())


def save_tmp_img(img):
    path = "{}/{}".format(TMP_PATH, generate_file_name())
    cv2.imwrite(path, img)
    return path

