from models.image import Image
import face_recognition as fr


def load_from_path(path):
    img_arr = fr.load_image_file(path)
    return Image(img_arr)

