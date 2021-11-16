import cv2
import cvzone
from numpy import eye

class detect_face():
    def __init__(self):

        self.face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.eye_detector = cv2.CascadeClassifier("opencv_haarcascade_eye.xml at 4.x · opencv_opencv.html")
        self.lip_detector = cv2.CascadeClassifier("opencv_haarcascade_smile.xml at 4.x · opencv_opencv.html")
        self.flag= 0

        video_cap = cv2.VideoCapture(0)
        while True:
            ret , self.frame = video_cap.read()

            if ret == False:
              break
    
            self.key = cv2.waitKey(1)
            if self.key ==ord("1") or self.flag == 1:
                self.sticker_face()
            if self.key ==ord("2") or self.flag == 2:
                self.sticker_eyes_lip()
            if self.key == ord("3") or self.flag == 3:
                self.checkered()
            if self.key == ord("4") or self.flag == 4:
                self.black_pen()
            if self.key == ord("5"):
                break
            cv2.imshow("sticker",self.frame)

    def sticker_face(self):
        self.flag = 1
        sticker = cv2.imread("Emoji Smiley-01.png",cv2.IMREAD_UNCHANGED)
        faces = self.face_detector.detectMultiScale(self.frame, 1.2,minNeighbors=10)
        for (x,y,w,h) in faces:
            sticker_resized = cv2.resize(sticker , (w,h))
            self.frame = cvzone.overlayPNG(self.frame,sticker_resized,[x,y])
            return self.frame

    def sticker_eyes_lip(self):
        self.flag = 2
        sticker2 = cv2.imread("eye.jpg")
        eyes = self.eye_detector.detectMultiScale(self.frame , 1.2 ,minNeighbors=45)
        for (x,y,w,h) in eyes:
            try:
                self.frame=cvzone.overlayPNG(self.frame,sticker2,[x,y])
            except:
                print("try egin")
        sticker3 = cv2.imread("lips.jpg")
        lips = self.lip_detector.detectMultiScale(self.frame , 1.8 , minNeighbors=22)
        for (lx , ly, lw,lh) in lips:
            try:
                self.frame = cvzone.overlayPNG(self.frame,sticker3,[lx+10,ly-15])
            except:
                print("try egin")
        return self.frame


    def checkered(self):
        self.flag = 3
        sticker4 = self.face_detector.detectMultiScale(self.frame , 1.3 , minNeighbors=5)
        for (x,y,w,h) in sticker4:
            blur = self.frame[y:y+h,x:x+w] 
            checkred = cv2.resize(blur ,(20 , 20),interpolation=cv2.INTER_LINEAR)
            result = cv2.resize(checkred , (w,h), interpolation=cv2.INTER_NEAREST)
            self.frame[y:y+h,x:x+w]= result
            return self.frame


    def black_pen(self):
        self.flag = 4
        black = cv2.GaussianBlur(self.frame,(21,21) , 0)
        self.frame = 255 - black
        return self.frame
            

detect_face()    


# img = cv2.imread('Mona_Lisa.jpg', 0)

# inverted = 255 - img
# blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
# inverted_blurred = 255 - blurred

# sketch = img / inverted_blurred
# sketch = sketch * 255
