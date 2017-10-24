##
# @author : Romain Francony, IT Student
# brief : transform image functions

import cv2
import numpy as np

img_gray = cv2.imread('./images/cat_small.jpg', 0)
img_bgr = cv2.imread('./images/cat_normal.jpg', 1)


# cv2.imshow("Gray levels image", img_gray)
# cv2.imshow("BGR image", img_bgr)
# cv2.waitKey(0)


def invert_colors_manual(input_img):
    img_inv = np.zeros(input_img.shape, dtype=np.uint8)

    # Gray scale image
    if len(input_img.shape) == 2:
        for x_index in xrange(img_inv.shape[0]):
            for y_index in xrange(img_inv.shape[1]):
                img_inv[x_index, y_index] = 255 - input_img[x_index, y_index]

        return img_inv

    # Color image
    for x_index in xrange(img_inv.shape[0]):
        for y_index in xrange(img_inv.shape[1]):
            for z_index in xrange(img_inv.shape[2]):
                img_inv[x_index, y_index, z_index] = 255 - input_img[x_index, y_index, z_index]

    return img_inv


def invert_colors_numpy(input_img):
    img_inv = (255 - input_img)
    return img_inv


def invert_colors_opencv(input_img):
    img_inv = cv2.bitwise_not(input_img)
    return img_inv


def threshold_image_manual(input_img):
    img_inv = np.zeros(input_img.shape, dtype=np.uint8)

    # Gray scale image
    if len(input_img.shape) == 2:
        for x_index in xrange(img_inv.shape[0]):
            for y_index in xrange(img_inv.shape[1]):
                if input_img[x_index, y_index] > 127:
                    img_inv[x_index, y_index] = 255
                else:
                    img_inv[x_index, y_index] = 0

        return img_inv

    # Color image
    for x_index in xrange(img_inv.shape[0]):
        for y_index in xrange(img_inv.shape[1]):
            for z_index in xrange(img_inv.shape[2]):
                if input_img[x_index, y_index, z_index] > 127:
                    img_inv[x_index, y_index, z_index] = 255
                else:
                    img_inv[x_index, y_index, z_index] = 0

    return img_inv


def threshold_image_numpy(input_img):
    return (input_img > 127).astype(np.uint8) * 255


def threshold_colors_opencv(input_img):
    return cv2.threshold(input_img, 127, 255, cv2.THRESH_BINARY)[1]
