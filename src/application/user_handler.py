from models.user import User
from models.image import Image
from application.face_handler import FaceHandler
from dataaccess.user import UserDao


class UserHandler:
    def __init__(self):
        face_embeddings = UserDao.load_all_user_embeddings()
        self.fh = FaceHandler(face_embeddings)

    def add_user_by_picture_name(self, img: Image, name):
        face_locs = self.fh.get_face_locations(img)
        assert len(face_locs) == 1

        #TODO: exception handli ng
        embedding = self.fh.get_face_encoding_by_location(img, face_locs[0])
        user = User(name, embedding)
        self.fh.add_face_by_user(user)
        UserDao(user).save()

    def get_users_by_picture(self, img: Image):
        users = []
        face_embeddings = self.fh.get_face_encodings(img)
        for embedding in face_embeddings:
            matched_id = self.fh.find_matched_id(embedding)
            user = None
            if matched_id:
                user = self.get_user_by_uuid(matched_id)
            users.append(user)
        return users

    @staticmethod
    def get_user_by_uuid(uuid):
        return UserDao.load_by_id(uuid)