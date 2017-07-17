import cv2

imgName = "Lena.png"
img = cv2.imread(imgName,cv2.IMREAD_GRAYSCALE)

# cv2.IMWRITE_JPEG_QUALITY
# For JPEG, it can be a quality from 0 to 100 (the higher is the better). Default value is 95.
cv2.imwrite('lena_jpg.jpg',img,(cv2.IMWRITE_JPEG_QUALITY,5))


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
