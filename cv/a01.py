import cv2

img = cv2.imread('face01.png')   # 將載入圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階 https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # 載入人臉模型
faces = face_cascade.detectMultiScale(gray)    # 偵測人臉

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('image', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()