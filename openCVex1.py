import cv2

image = cv2.imread('./media/ariana_grande_leggy_modeling_04-cf03c25a.jpg', 0)
cv2.imshow('image', image)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
