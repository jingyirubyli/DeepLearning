import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('pic0100.png')

    img_car1 = img[15:30, 30:50]

    cv2.imshow('image', img_car1)

    cv2.imwrite('pic0200.png',img_car1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()