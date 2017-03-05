import cv2
import numpy as np
import pywt

imgName = "Lena.png"
img = cv2.imread(imgName,cv2.IMREAD_GRAYSCALE)
imf = np.float32(img)

coeffs = pywt.dwt2(imf, 'haar')
cA, (cH, cV, cD) = coeffs
# 						|cA(LL)|cH(LH)|
# cA, (cH, cV, cD)<---> ---------------
# 						|cV(HL)|cD(HH)|
idwt = pywt.idwt2(coeffs, 'haar')

dst =  np.uint8(idwt)
print(dst.shape)

cv2.imshow('dct',dst)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()