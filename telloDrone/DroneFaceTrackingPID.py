from utils import *
import utils
import unittest
import time

def main():
    frameCounter = 0
    num_frames = 150
    w, h = 1024, 768
    pid = [0.5, 0.5, 0]  # kd, kp,ki
    pError = 0
    # if False then the webcam is used as image feed
    utils.useDrone = False

    myDrone = intializeTello()
    if utils.useDrone:
        myDrone.takeoff()
        time.sleep(3)

    while True:

        if frameCounter == 0:
            start = time.time()

        ## STEP 1
        img = telloGetFrame(myDrone, w, h)
        frameCounter += 1

        # STEP 2
        img, info = findBiggestFace(img)
        #print(info[0][0])  # x value of center point of the closest face with largest area

        # STEP 3
        pError = trackFace(myDrone, info, w, pid, pError)

        # DISPLAY IMAGE
        cv2.imshow("MyResult", img)

        if frameCounter == num_frames:
            end = time.time()
            # Time elapsed
            seconds = end - start
            #print('Time taken: ' + str(round(seconds,2)) + ' seconds')
            # Calculate frames per second
            fps = num_frames / seconds
            print('Estimated frames per second: ' + str(round(fps,2)) + ' .... Time taken: ' + str(round(seconds,2)) + ' seconds')
            frameCounter = 0

        # WAIT FOR THE 'Q' BUTTON TO STOP
        if cv2.waitKey(1) & 0xFF == ord('q'):
            terminate(myDrone)
            break

    print("Finished main.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
