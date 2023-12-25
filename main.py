import cv2
image = cv2.imread("img1.png")
#preprocess
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
blur = cv2.medianBlur(gray, 5)
##
