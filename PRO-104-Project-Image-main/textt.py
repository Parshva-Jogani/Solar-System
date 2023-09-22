import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "Mercury", (110,180), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "venus", (190,270), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "earth", (300,270), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "mars", (400,270), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "jupiter", (590,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "saturn", (720,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "uranus", (950,130), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 
cv2.putText(img, "neptune", (1080,130), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255)) 

cv2.imshow("space", img)
cv2.waitKey(0)

cv2.imwrite("new_system.jpg", img)