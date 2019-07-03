import cv2
import numpy as np

def resize(img, scale=0.2):
    return cv2.resize(img, (0,0), None, scale, scale)


img = cv2.imread('hollywood.JPG')

height, width, chan = img.shape

cropped = img[0:height, 0:height, 0]

inverse = np.linalg.inv(cropped)

doubleInverse = np.linalg.inv(inverse)

# gCropped = np.linalg.inv(cropped[1])
# bCropped = np.linalg.inv(cropped[2])


# print(cropped.shape)

# inverted = np.linalg.inv(cropped)

while True:
    cv2.imshow('original', resize(doubleInverse))
    cv2.imshow('cropped', resize(cropped))
    cv2.imshow('inverted', resize(inverse))

    cv2.waitKey(0)
