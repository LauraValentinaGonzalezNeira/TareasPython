import cv2
import numpy as np

img =cv2.imread('montanas.jpg')
tam = cv2.resize(img,(500,500))

imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GARY)
tam1 = cv2.resize(imgGRAY,(500,500))
cv2.imshow("En grices",tam1 )

kernel = np.ones((5,5),np.unit8)

imgCanny = cv2.Canny(img, 150,200)
tam2 = cv2.resize(imgCanny,(500,500))
cv2.imshow('Canny',tam2)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
tam3 = cv2.resize(imgDialation,(500,500))
cv2.imshow("Dialation",tam3)

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
tam4 = cv2.resize(imgEroded,(500,500))
cv2.imshow("Eroded",tam4)

imgr = cv2.rectangle(img,(10,10),(150,200),(0,0,255),cv2.FILLED) 
tam5 = cv2.resize(imgr,(500,500))
cv2.imshow("Rectangulo",tam5)

cv2.waitKey(0)





