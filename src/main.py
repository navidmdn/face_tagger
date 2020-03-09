import cv2

from util.image import load_from_path
from application import face_handler as fh

img = load_from_path('../data/images/DSC_0946.JPG')
locs = fh.get_face_locations(img)

for idx, loc in enumerate(locs):
    current = fh.get_face_at_location(img, loc)
    cv2.imwrite('../data/'+str(idx)+'.jpg', current[:,:,::-1])

# fh.get_face_encodings(img)