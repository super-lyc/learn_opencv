import cv2 as cv
filename=r'C:\Users\luoyongchen\Pictures\asuka.jpg'
img=cv.imread(filename)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)    # BGR to GRAY
cv.imshow('source',img)
cv.imshow('gray',gray)
cv.waitKey()
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)    # bgr to hsv
cv.imshow('HUE',hsv[:,:,0])
cv.imshow('Saturation',hsv[:,:,1])
cv.imshow('Value',hsv[:,:,2])
cv.waitKey()
cv.imshow('Blue',img[:,:,0])
cv.imshow('Green',img[:,:,1])
cv.imshow('Red',img[:,:,2])
cv.waitKey()
cv.destroyAllWindows()