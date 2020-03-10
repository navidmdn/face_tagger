from util.mongo import db
from models.user import User
import numpy as np

COLLECTION_NAME = 'user'
client = db[COLLECTION_NAME]


class UserDao:
    def __init__(self, user):
        self._id = user.uuid
        self.name = user.name
        self.face_embedding = list(user.face_embedding)

    def to_dao(self):
        return {
            '_id': self._id,
            'name': self.name,
            'face_embedding': self.face_embedding
        }

    @staticmethod
    def from_dao(obj):
        return User(
            name=obj['name'],
            face_embedding=np.array(obj['face_embedding']),
            uuid=obj['_id']
        )

    def save(self):
        client.insert_one(self.to_dao())

    @staticmethod
    def load_by_id(uuid):
        result = client.find_one({'_id': uuid})
        return UserDao.from_dao(result)

    @staticmethod
    def load_all_user_embeddings():
        results = client.find()
        return list(map(lambda user_obj: UserDao.from_dao(user_obj), results))

