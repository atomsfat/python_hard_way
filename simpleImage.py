import numpy
import cv2

img = numpy.zeros((3, 3), dtype=numpy.uint8)
img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

print(img)
print(img2)
img2.shape
cv2.imshow('image', img2)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
