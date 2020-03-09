import face_recognition as fr


def get_face_locations(img):
    digest = img.get_digest()
    face_locations = fr.face_locations(digest)
    locs = []
    for location in face_locations:
        top, right, bottom, left = location
        locs.append([
            int(top * img.shape[0] / img.digest_y),
            int(right * img.shape[1] / img.digest_x),
            int(bottom * img.shape[0] / img.digest_y),
            int(left * img.shape[1] / img.digest_x),
        ])
    return locs


def get_face_at_location(img, loc, margin=100):
    top, right, bottom, left = loc
    result = img.arr[
             max(top - margin, 0):bottom + margin,
             max(left - margin, 0):right + margin]
    return result


def get_face_windows(img):
    locs = get_face_locations(img)
    faces = []
    for loc in locs:
        faces.append(get_face_at_location(img, loc))
    return faces


def get_face_encodings(img):
    face_locations = get_face_locations(img)
    return fr.face_encodings(img.arr, face_locations)