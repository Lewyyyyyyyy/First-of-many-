import cv2
from random import randrange
#import pre-trained data on faces
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



# 0 to use webcam as input for video or you can also use a savd video
webcam=cv2.VideoCapture(0)
#webcam=cv2.VideoCapture('vid.mp4')
#iterate on every frame of the video
while True:
    success, frame = webcam.read()
    #success is a bool value and frame is our image

    #detect faces
    imgray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coor = trained_face_data.detectMultiScale(imgray)

    for (x, y, w, h) in face_coor:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    # hedhi lezma bch todhher l image , hiya rahi dhohret ama fissa3 inti ma tchoufhech
    key=cv2.waitKey(1)
    if (key==81 or key==8) :
        break
webcam.release()





























print("Code jawo behi")
