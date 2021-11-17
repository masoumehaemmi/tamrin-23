import cv2
import cvzone
from numpy import eye

class detect_face():
    def __init__(self):

        self.face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.eye_detector = cv2.CascadeClassifier("eyes.xml")
        self.lip_detector = cv2.CascadeClassifier("lip.xml")
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
        sticker2 = cv2.imread("eye.png",cv2.IMREAD_UNCHANGED)
        eyes = self.eye_detector.detectMultiScale(self.frame , 1.2 ,minNeighbors=10)
        for eye in eyes:
            x,y,w,h=eye
            try:
                eye_resized = cv2.resize(sticker2,(w,h))
                self.frame=cvzone.overlayPNG(self.frame,eye_resized,[x,y])
            except Exception as e:
                print(e)
        sticker3 = cv2.imread("lip.png",cv2.IMREAD_UNCHANGED)
        lips = self.lip_detector.detectMultiScale(self.frame , 1.8 , minNeighbors=50)
        for (lx , ly, lw,lh) in lips:
            try:
                lip_resized = cv2.resize(sticker3 , (lw,lh))
                self.frame = cvzone.overlayPNG(self.frame,lip_resized,[lx+20,ly-25])
            except Exception as e :
                 print(e)
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
