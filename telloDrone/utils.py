from djitellopy import Tello
import cv2
import numpy as np
import os, sys

#https://www.murtazahassan.com/drone-face-tracking-pid-using-opencv-p-1/

#if False then the webcam is used as image feed
useDrone = False
#cap = cv2.VideoCapture(0)
#solves warning but might slow down the framerate
#but seems not to be the case for me (compared frame rate measurement in main() )
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # ==> https://stackoverflow.com/questions/53888878/cv2-warn0-terminating-async-callback-when-attempting-to-take-a-picture

def intializeTello():
    # CONNECT TO TELLO
    myDrone = Tello()
    if useDrone:
        myDrone.connect()
        myDrone.for_back_velocity = 0
        myDrone.left_right_velocity = 0
        myDrone.up_down_velocity = 0
        myDrone.yaw_velocity = 0
        myDrone.speed = 0
        print(myDrone.get_battery())
        myDrone.streamoff()
        myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone,w=360,h=240):
    if useDrone:
        # GET THE IMGAE FROM TELLO
        myFrame = myDrone.get_frame_read()
        myFrame = myFrame.frame
    else:
        #fps = cap.get(cv2.CAP_PROP_FPS)
        #print('Frames per second using cap.get(cv2.CAP_PROP_FPS): ' + str(fps))
        success, myFrame = cap.read()

    img = cv2.resize(myFrame, (w, h))
    return img

def findFaces(img):
    #faceCascade = cv2.CascadeClassifier('..\openCV\Resources\haarcascades\haarcascade_frontalface_default.xml')
    dirName = os.path.dirname(__file__)
    #print("findFaces dirName: " + dirName)
    # needed to downgrade pip3 install opencv-contrib-python==4.1.2.30
    # otherwise OpenCV with Python wont exit properly when using detectMultiScale on CascadeClassifier
    # https://stackoverflow.com/questions/62211684/opencv-with-python-wont-exit-properly-when-using-detectmultiscale-on-cascadeclas
    faceCascade = cv2.CascadeClassifier(os.path.join(dirName, '../openCV/Resources/haarcascades/haarcascade_frontalface_default.xml'))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)

    #center
    myFaceListC = []
    myFaceListArea = []

    for (x,y,w,h) in faces:
        cx = x + w//2
        cy = y + h//2
        area = w*h
        myFaceListArea.append(area)
        myFaceListC.append([cx,cy])
        cv2.putText(img, str(area), (x - 5, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (0, 0, 255))
        cv2.rectangle(img,(x,y), (x+w,y+h), (0,0,255), 2)

    return img, faces, myFaceListC, myFaceListArea

def findBiggestFace(img):

    img, faces, myFaceListC, myFaceListArea = findFaces(img)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0,0],0]

def trackFace(myDrone,info,w,pid,pError):
    # PID
    #         cx
    error = info[0][0] - w//2
    speed = pid[0]*error + pid[1]*(error-pError)
    speed = np.clip(speed, -100, 100)
    #print(speed)

    if useDrone:
        if info[0][0] !=0:
            myDrone.yaw_velocity = speed
        else:
            myDrone.for_back_velocity = 0
            myDrone.left_right_velocity = 0
            myDrone.up_down_velocity = 0
            myDrone.yaw_velocity = 0
            error = 0
        if myDrone.send_rc_control:
            myDrone.send_rc_control(
                myDrone.left_right_velocity,
                myDrone.for_back_velocity,
                myDrone.up_down_velocity,
                myDrone.yaw_velocity)

    return error

def terminate():
    print('Terminate')
    if useDrone:
        myDrone.land()
    cap.release()
    cv2.destroyAllWindows()
