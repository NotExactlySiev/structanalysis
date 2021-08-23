import snum
import smath
import cv2

snums = {}

def get_snum(num):
    if num not in snums.keys():
        snums[num] = snum.snum(num)

    return snums[num]

def shown(num, zoom=12):
    num = get_snum(num)
    shape = smath.color_matrix(num.get_indexes(), num.get_count())
    resized = cv2.resize(shape, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_NEAREST)
    resized = 255 - smath.increase_contrast(resized)
    cv2.imshow("", resized)

def stdn(num):
    return get_snum(num).get_std()

def entn(num):
    return get_snum(num).get_entropy()
