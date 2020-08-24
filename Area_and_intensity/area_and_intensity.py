import numpy as np
import cv2

img = cv2.imread('/home/gc/Desktop/gray_scale_img.jpg')
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

threshed_img = cv2.adaptiveThreshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,2)

contour, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(" Gray scale intensity at each level and their area")

for c in contour:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    #draw a green rectangle to visualize the bounding rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    area = cv2.contourArea(c)
    print('area',area)
       
    # get the min area rect
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    print('grey scale intensity',gray[y][x])
    
cv2.drawContours(img, contour, -1, (0, 255, 0), 2) 
  
cv2.imshow('Contours', img)

   
cv2.waitKey(0)

cv2.destroyAllWindows()
