import cv2
import numpy as np
import pywt

imgName = "Lena.png"
img = cv2.imread(imgName,cv2.IMREAD_GRAYSCALE)
imf = np.float32(img)

coeffs = pywt.wavedec2(imf, 'db1',level=None)
# 	[cAn, (cHn, cVn, cDn), ... (cH1, cV1, cD1)] : list
# 						|cA(LL)|cH(LH)|
# cA, (cH, cV, cD)<---> ---------------
# 						|cV(HL)|cD(HH)|
idwt = pywt.waverec2(coeffs, 'db1')
dst =  np.uint8(idwt)
print(len(coeffs)-1)

cv2.imshow('dct',dst)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()