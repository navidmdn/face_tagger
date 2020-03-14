from uuid import uuid4


class User:
    def __init__(self, name: str, face_embedding, phone_number=None, uuid=None):
        self.uuid = uuid if uuid else str(uuid4())
        self.name = name.lower()
        self.phone_number = phone_number
        self.face_embedding = face_embedding

    def __repr__(self):
        return "id:{}, name:{}".format(self.uuid, self.name)