import cv2

image=cv2.imread("C:/Users/Ntech/PycharmProjects/object_detection/90636361.jfif")
image

while True:
    cv2.imshow("image",image)

    text="This is me"
    cv2.putText(image,text,(40,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,0,0),1)

    cv2.rectangle(image,(50,50),(500,500),(0,0,255),2)
    cv2.imwrite("output_image.jpg",image)


    key=cv2.waitKey(1)
    if key==ord('q'):
        break


