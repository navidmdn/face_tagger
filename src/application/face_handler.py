import face_recognition as fr


def get_face_locations(img):
    digest = img.get_digest()
    face_locations = fr.face_locations(digest)
    locs = []
    for location in face_locations:
        top, right, bottom, left = location
        print(location)
        locs.append([
            top * img.shape[0] / img.digest_y,
            right * img.shape[1] / img.digest_x,
            bottom * img.shape[0] / img.digest_y,
            left * img.shape[1] / img.digest_x,
        ])
    return locs


def get_face_at_location(img, loc, margin=30):
    top, right, bottom, left = loc
    print(loc)
    result = img.arr[
             max(int(top) - margin, 0):int(bottom) + margin,
             max(int(left) - margin, 0):int(right) + margin]
    return result
