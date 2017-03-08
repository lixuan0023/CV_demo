import cv2

imgName = "Lena.png"
img = cv2.imread(imgName,cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
