from djitellopy import Tello
import cv2
import time

######################################################################
width = 320  # WIDTH OF THE IMAGE
height = 240  # HEIGHT OF THE IMAGE
startCounter = 0  # 0 FOR FLIGHT 1 FOR TESTING
######################################################################

# CONNECT TO TELLO
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())

#me.streamoff()
#me.streamon()

while True:

    # GET THE IMGAE FROM TELLO
    #frame_read = me.get_frame_read()
    #myFrame = frame_read.frame
    #img = cv2.resize(myFrame, (width, height))

    # DISPLAY IMAGE
    #cv2.imshow("MyResult", img)

    # TO GO UP IN THE BEGINNING
    if startCounter == 0:
        me.takeoff()
        time.sleep(5)
        me.move_back(160)
        time.sleep(5)
        me.rotate_counter_clockwise(90)
        time.sleep(5)
        me.flip_forward()
        time.sleep(5)
        me.flip_forward()
        time.sleep(5)
        me.flip_right()
        time.sleep(5)
        me.flip_left()
        time.sleep(5)
        me.flip_back()
        time.sleep(5)
        me.flip_back()
        #me.move_forward(195)
        #time.sleep(5)
        #me.rotate_clockwise(90)
        #time.sleep(5)
        #me.move_forward(100)
        #time.sleep(5)
        #me.rotate_counter_clockwise(90)
        #time.sleep(5)
        #me.move_forward(100)
        #
        #time.sleep(5)
        #me.flip_forward()
        #me.rotate_clockwise(90)
        #time.sleep(3)
        #me.rotate_counter_clockwise(90)
        #time.sleep(3)
        #me.move_left(35)
        #time.sleep(3)
        #me.move_right(35)
        #time.sleep(3)
        #me.flip_forward()
        #time.sleep(3)
        #me.flip_back()
        #time.sleep(3)
        #me.flip_right()
        #time.sleep(3)
        #me.flip_left()
        time.sleep(3)
        me.land()
        startCounter = 1


    # # SEND VELOCITY VALUES TO TELLO
    # if me.send_rc_control:
    #     me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)

    # DISPLAY IMAGE
    #cv2.imshow("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break