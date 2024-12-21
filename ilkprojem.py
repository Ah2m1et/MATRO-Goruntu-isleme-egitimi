import cv2

img = cv2.imread('mustang.jpg')

img[20,30] = [255,255,255]

for i in range(100):
    img[30,i] = [255,255,255]
    img[31,i] = [255,255,255]
    img[32,i] = [255,255,255]


img[100:200, 200:300, 2] = 255

img[:,:,1] = 200
 
cv2.imshow("arabam",img)
cv2.waitKey(0)