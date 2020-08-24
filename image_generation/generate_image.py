import numpy as np
import cv2

height=300
width = 300

blank_image = np.zeros((height,width,1), np.uint8)

blank_image[0:height//8,:] = (25)      # (B, G, R)
blank_image[height//8:2*height//8,:] = (50)
blank_image[2*height//8:3*height//8,:] = (75)
blank_image[3*height//8:4*height//8,:] = (125)
blank_image[4*height//8:5*height//8,:] = (150)
blank_image[5*height//8:6*height//8,:] = (175)
blank_image[6*height//8:7*height//8,:] = (200)
blank_image[7*height//8:height,:] = (255)

img = blank_image

cv2.imshow('image',img)
cv2.imwrite('/home/gc/Desktop/gray_scale_img.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
