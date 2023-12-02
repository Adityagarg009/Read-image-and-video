import cv2 as cv
img = cv.imread('content/naruto.jpg')
cv.imshow('naruto', img)
cv.waitKey(0)
capture=cv.VideoCapture('content/n.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(10) and 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()