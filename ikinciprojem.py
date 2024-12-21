import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)

cv2.rectangle(img,(50,50),(500,500),(255,0,0),4)
cv2.circle(img,(256,256),50,(0,255,0),8)
cv2.line(img,(125,125),(325,325),(255,255,255),5)

cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)

cv2.imshow("resmim",img)

cv2.waitKey(0)













"""
img = cv2.imread('Recep-ivedik.jpg')

gray = cv2.imread('Recep-ivedik.jpg',0)

#print(img)
print(img.size)
print(img.shape)
print(img.dtype)

print("ikinci fotograf")
print(gray.shape)
print(gray.size)


cv2.imshow("gray",gray)
cv2.imshow("recep",img)
cv2.waitKey(0)

"""