import cv2
cars_data=cv2.CascadeClassifier('cas4.xml')
ped_data=cv2.CascadeClassifier('haarcascade_fullbody.xml')
inp=cv2.imread("d.jfif")

imp_gray=cv2.cvtColor(inp,cv2.COLOR_BGR2GRAY)
peds=ped_data.detectMultiScale(imp_gray)
cars=cars_data.detectMultiScale(imp_gray)



for(x,y,w,h) in cars :
    cv2.rectangle(inp,(x,y),(x+w,y+h),(255,0,0),2)
for(x,y,w,h) in peds :
    cv2.rectangle(inp,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('cars',inp)
cv2.waitKey()

"""
vid=cv2.VideoCapture("")
while True:
    succes,frame=vid.read()
    if succes:
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        peds = ped_data.detectMultiScale(gray_frame)
        cars = trained_data.detectMultiScale(gray_frame)
        for (x, y, w, h),(x1,y1,w1,h1) in cars,peds :
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
        else :
            break
        cv2.imshow('cars_vid_detector',frame)
        key=cv2.waitKey(1)
        if key==81 or key==8:
    break
"""









