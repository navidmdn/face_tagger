from src.models.image import Image
import cv2
from uuid import uuid4


def load_from_path(path):
    img_arr = cv2.imread(path)
    return Image(img_arr)


def generate_file_name():
    return '{}.jpg'.format(uuid4())