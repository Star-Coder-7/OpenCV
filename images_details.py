import cv2
import random

img = cv2.imread('images/python_logo.jpeg', -1)

# print(img)
# BLUE, GREEN, RED - REPRESENTING PIXELS IN THE RANGE OF 0-255

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()