import cv2


MIN_DIGEST_X = 400
MIN_DIGEST_Y = 400


class Image:
    def __init__(self, img_arr):
        self.arr = img_arr
        self.shape = img_arr.shape

        if img_arr.shape[0] > img_arr.shape[1]:
            self.ratio = MIN_DIGEST_X / img_arr.shape[1]
        else:
            self.ratio = MIN_DIGEST_Y / img_arr.shape[0]

        self.digest = None

    def get_digest(self):
        if self.digest:
            return self.digest
        self.digest = cv2.resize(self.arr, (0,0), fx=self.ratio, fy=self.ratio)
        return self.digest

