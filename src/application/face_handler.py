import face_recognition as fr
import numpy as np
from src.models.image import Image
from collections import OrderedDict


class FaceHandler:
    def __init__(self, face_embeddings):
        self.faces = OrderedDict(
            map(lambda user: (user.uuid, user.face_embedding), face_embeddings)
        )

    def add_face_by_user(self, user):
        self.faces[user.uuid] = user.face_embedding

    def find_matched_id(self, face_embedding):
        match_id = None
        known_embeddings = list(self.faces.values())
        if len(known_embeddings) == 0:
            return None
        matches = fr.compare_faces(known_embeddings, face_embedding, tolerance=0.5)
        face_distances = fr.face_distance(known_embeddings, face_embedding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            match_id = list(self.faces.keys())[best_match_index]
        return match_id

    @staticmethod
    def get_face_locations(img: Image):
        digest = img.get_digest()
        face_locations = fr.face_locations(digest)
        locs = []
        for location in face_locations:
            top, right, bottom, left = location
            locs.append([
                int(top / img.ratio),
                int(right / img.ratio),
                int(bottom / img.ratio),
                int(left / img.ratio),
            ])
        return locs

    @staticmethod
    def get_face_at_location(img: Image, loc, margin=10):
        top, right, bottom, left = loc
        result = img.arr[
                 max(top - margin, 0):bottom + margin,
                 max(left - margin, 0):right + margin]
        return result

    @staticmethod
    def get_face_windows(img: Image):
        locs = FaceHandler.get_face_locations(img)
        faces = []
        for loc in locs:
            faces.append(FaceHandler.get_face_at_location(img, loc))
        return faces

    @staticmethod
    def get_face_encodings_by_location(img: Image, locations):
        return fr.face_encodings(img.arr, locations)

    @staticmethod
    def get_face_encoding_by_location(img: Image, location):
        return fr.face_encodings(img.arr, [location])[0]
