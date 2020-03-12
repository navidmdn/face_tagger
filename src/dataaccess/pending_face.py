from src.util.mongo import db
from src.models.pending_face import PendingFace
import numpy as np
import cv2

COLLECTION_NAME = 'pending_face'
client = db[COLLECTION_NAME]


class PendingFaceDao:
    def __init__(self, pending_face):
        self.img_path = pending_face.img_path
        self.face_embedding = list(pending_face.face_embedding)
        self.processed = False
        self.img = pending_face.img

    def to_dao(self):
        return {
            'img_path': self.img_path,
            'processed': self.processed,
            'face_embedding': self.face_embedding
        }

    @staticmethod
    def from_dao(obj):
        pass
        # return User(
        #     name=obj['name'],
        #     face_embedding=np.array(obj['face_embedding']),
        #     uuid=obj['_id']
        # )

    def save(self):
        print(self.img_path)
        client.insert_one(self.to_dao())
        cv2.imwrite(self.img_path, self.img)