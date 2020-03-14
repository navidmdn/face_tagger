from src.util.mongo import db
from src.models.pending_face import PendingFace
import numpy as np
from src.util import image
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
        if obj is None:
            return None
        pending_face = PendingFace(
            face_embedding=obj['face_embedding'],
        )
        pending_face.img_path = obj['img_path']
        pending_face._id = obj['_id']
        return pending_face

    def save(self):
        print(self.img_path)
        client.insert_one(self.to_dao())
        cv2.imwrite(self.img_path, self.img)

    @staticmethod
    def load_random_unprocessed():
        result = client.find_one({'processed': False})
        return PendingFaceDao.from_dao(result)

    @staticmethod
    def finish_process(_id):
        client.update_one(filter={'_id': _id}, update={'$set': {'processed': True}})