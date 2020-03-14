from src.models.image import Image
from src.application.user_handler import user_handler
from src.models.pending_face import PendingFace
from src.util import image as img_util
from src.dataaccess.pending_face import PendingFaceDao


class PendingFaceHandler:
    def __init__(self):
        self.pending = {}

    def add_image(self, img: Image):
        new_face = False
        pairs = user_handler.get_face_window_user_embedding_pairs(img)
        for pair in pairs:
            # if user not found
            if not pair[1]:
                new_face = True
                pending_face = PendingFace(img_util.generate_file_name(), pair[2], pair[0])
                PendingFaceDao(pending_face).save()

        if new_face:
            return 0
        return -1

    def get_random_pending_face(self):
        pending_face = PendingFaceDao.load_random_unprocessed()
        return pending_face

    def submit_info(self, username):
        PendingFaceDao.finish_process(self.pending[username]._id)
        self.pending[username] = None
