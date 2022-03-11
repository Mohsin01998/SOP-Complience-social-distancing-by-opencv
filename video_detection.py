import cv2
import imutils

cap=cv2.VideoCapture("test_video.mp4")


while True:
    ret, frame = cap.read()
    frame=imutils.resize(frame,width=500)




    text="This is me"
    cv2.putText(frame,text,(40,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,0,0),1)

    cv2.rectangle(frame,(50,50),(500,500),(0,0,255),2)


    cv2.imshow("Object",frame)



    key=cv2.waitKey(1)
    if key==ord('q'):
        break


