import cv2
import numpy as np 

img = np.zeros([512,512,3],np.uint8)

cv2.putText(img,"Matronun egitimleri cok guzel",(50,256),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

aynalanmisGoruntu = cv2.flip(img,-1)

cv2.imshow("aynalanmis goruntu",aynalanmisGoruntu)
cv2.imshow("isim",img)
cv2.waitKey(0)


