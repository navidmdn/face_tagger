import cv2

from src.util.image import load_from_path
from src.application.user_handler import UserHandler

navid_img = load_from_path('../data/0.jpg')
nasi_img = load_from_path('../data/1.jpg')
couple = load_from_path('../data/images/DSC_0921.JPG')
# locs = fh.get_face_locations(img)

# for idx, loc in enumerate(locs):
#     current = fh.get_face_at_location(img, loc)
#     cv2.imwrite('../data/'+str(idx)+'.jpg', current[:,:,::-1])

# fh.get_face_encodings(img)
uh = UserHandler()

# uh.add_user_by_picture_name(navid_img, 'navid')
# uh.add_user_by_picture_name(nasi_img, 'nastaran')

users = uh.get_face_window_user_embedding_pairs(couple)

for user in users:
    print(user)

