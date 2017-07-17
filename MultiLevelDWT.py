import cv2
import numpy as np
import pywt

imgName = "Lena.png"
img = cv2.imread(imgName,cv2.IMREAD_GRAYSCALE)
imf = np.float32(img)

coeffs = pywt.wavedec2(imf, 'db1',level=3)
# 	[cAn, (cHn, cVn, cDn), ... (cH1, cV1, cD1)] : list
# 						|cA(LL)|cH(LH)|
# cA, (cH, cV, cD)<---> ---------------
# 						|cV(HL)|cD(HH)|


cAi = coeffs[0]
for i in range(1,4):
	(cHi, cVi, cDi) = coeffs[i]
	Row1 = np.concatenate((cAi,cHi),axis=1)
	Row2 = np.concatenate((cVi,cDi),axis=1)
	cAi_1 = np.concatenate((Row1,Row2),axis=0)
	cAi = cAi_1

print(cAi.shape)



#  np.concatenate((a,b),axis=0)
#  axis = 0 -> |a|  axis = 1 -> |a|b| 
#              |b|


# idwt = pywt.waverec2(coeffs, 'db1')
# dst =  np.uint8(idwt)
# print(len(coeffs)-1)

dst = np.uint8(cAi)
dst = np.concatenate((dst,img),axis=1)

# cv2.imshow('image',img)
cv2.imshow('dct',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()