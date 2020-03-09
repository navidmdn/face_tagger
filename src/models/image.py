import cv2


DIGEST_X = 400
DIGEST_Y = 400


class Image:
    def __init__(self, img_arr):
        self.arr = img_arr
        self.shape = img_arr.shape
        self.digest = None
        self.digest_x = DIGEST_X
        self.digest_y = DIGEST_Y

    def get_digest(self):
        if self.digest:
            return self.digest
        self.digest = cv2.resize(self.arr, (self.digest_x, self.digest_y))
        return self.digest

