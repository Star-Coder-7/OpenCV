import cv2
import random

img = cv2.imread('images/tech_tim.jpg', -1)

logo = img[500:700, 600:900]
img[100:300, 650:950] = logo

# print(img)
# BLUE, GREEN, RED - REPRESENTING PIXELS IN THE RANGE OF 0-255

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()