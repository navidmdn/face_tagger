from src.config import PENDING_FACE_PATH
import os


class PendingFace:
    def __init__(self, img_name=None, face_embedding=None, img=None):
        if img_name:
            self.img_path = os.path.join(PENDING_FACE_PATH, img_name)
        self.face_embedding = face_embedding
        self.processed = False
        self.img = img
        self.pending_user_info = {}
