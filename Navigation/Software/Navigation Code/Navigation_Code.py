#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import serial
import string
from threading import Thread
import numpy as np
import cv2

# Open the serial port between the Raspberry Pi 4B and the Arduino

ser = serial.Serial('/dev/ttyACM0', 9600)
temp = serial.Serial('/dev/ttyUSB3', 9600)
hum = serial.Serial('/dev/ttyUSB2', 9600)
mc = serial.Serial('/dev/ttyUSB1', 9600)
time.sleep(0.2)

FRONT_GPIO = 15
LEFT_CORNER_GPIO = 13
RIGHT_CORNER_GPIO = 16

temps = []
hums = []
mcs = []

print(temps)
print(hums)
print(mcs)


def takePic(dc):
    print("In this biotch")
# creating the videocapture object
    # and reading from the input file
    # Change it to 0 if reading from webcam
    cap = cv2.VideoCapture("v4l2src ! image/jpeg, width=1280, height=720, framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw, format=BGR ! appsink ")

    #cap2 = cv2.VideoCapture("v4l2src device=/dev/video2 ! image/jpeg, width=1280, height=720, framerate=30/1 ! jpegdec ! videoconvert ! video/x-raw, format=BGR ! appsink ")


    # used to record the time when we processed last frame
    prev_frame_time = 0
    #prev_frame_time2 = 0 
    # used to record the time at which we processed current frame
    new_frame_time = 0
    #new_frame_time2 = 0
    # Declaring Base Path Name for Wall and Ceiling Frames
    #wall_frame_base_path = ("/home/ubuntu/Desktop/ECE_4961_4971_Autonomous_Crawlspace_Inspection_Robot/Crawlspace_Images")
    #wall_frame_base_name = ("wall_frame")
    ceiling_frame_base_path = ("/home/ubuntu/Desktop/ECE_4961_4971_Autonomous_Crawlspace_Inspection_Robot/Crawlspace_Images")
    ceiling_frame_base_name = ("ceiling_frame")

    # Reading the video file until finished
    while(cap.isOpened()): #& cap2.isOpened()):
 
        # Capture frame-by-frame
        ret, frame = cap.read()
        #ret2, frame2 = cap2.read()
 
        # if video finished or no Video Input
        if not ret: # & ret2:
            break
 
        # Our operations on the frame come here
        gray = frame
        #gray2 = frame2
        # resizing the frame size according to our need
        gray = cv2.resize(gray, (1280,720))
        #gray2 = cv2.resize(gray2, (1280,720))
 
        # font which we will be using to display FPS
        font = cv2.FONT_HERSHEY_SIMPLEX
        #font2 = cv2.FONT_HERSHEY_SIMPLEX
        # time when we finish processing for this frame
        new_frame_time = time.time()
        #new_frame_time2 = time.time()
        # Calculating the fps
 
        # fps will be number of frame processed in given time frame
        # since their will be most of time error of 0.001 second
        # we will be subtracting it to get more accurate result
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
     
        #fps2 = 1/(new_frame_time2-prev_frame_time2)
        #prev_frame_time2 = new_frame_time2
 
 
        # converting the fps into integer
        fps = int(fps)
        #fps2 = int(fps2)
        # converting the fps to string so that we can display it on frame
        # by using putText function
        fps = str(fps)
        #fps2 = str(fps2)
        # putting the FPS count on the frame
        cv2.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
        #cv2.putText(gray2, fps2, (7, 70), font2, 3, (100, 255, 0), 3, cv2.LINE_AA)
        # displaying the frame with fps
        cv2.imshow('frame', gray)
        #cv2.imshow('frame2', gray2)
        # function for capturing/saving image

        #if cv2.waitKey(1) & 0xFF == ord('c'):
            #break
        print("About to If")
        if cv2.waitKey(1):
            ceiling_outfile = '%s/%s.jpg' % (ceiling_frame_base_path, str(dc))
            #wall_outfile = '%s/%s.jpg' % (wall_frame_base_path, wall_frame_base_name + str(dc))
            time.sleep(3)
            print("Slept")
            cv2.imwrite(ceiling_outfile, frame)
            #v2.imwrite(wall_outfile, frame2)
        print("About To If 2")
        # press 'Q' if you want to exit
        if cv2.waitKey(1): #& 0xFF == ord('q'):
            break
 
    # When everything done, release the capture
    cap.release()
    # Destroy the all windows now
    cv2.destroyAllWindows()
    print("About To Return")

# Function To Get and Print Data - Will Execute 100 Times Then Clearn Up
def getandPrint():

    print("SeeedStudio Grove Ultrasonic Get Data and Print")

    # test 100 times
    for i in range(100):
        measurementInCM()

    # Reset GPIO Settings
    # Clean Ups All Pins I Have Set In This .Py
    GPIO.cleanup()

# Function To Get Measurements From GPIO Pins (Start and Stop)
def measurementInCM(): 

    # Setup GPIO_SIGs As Outputs
    GPIO.setup(FRONT_GPIO, GPIO.OUT)
    GPIO.setup(LEFT_CORNER_GPIO,GPIO.OUT)
    GPIO.setup(RIGHT_CORNER_GPIO,GPIO.OUT)

    # Output Low on GPIO_SIGs, Then High, Then Return Low State
    GPIO.output(FRONT_GPIO, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(FRONT_GPIO, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(FRONT_GPIO, GPIO.LOW)
    start = time.time()
    GPIO.setup(FRONT_GPIO, GPIO.IN)

    while GPIO.input(FRONT_GPIO) == 0:
        start = time.time()

    while GPIO.input(FRONT_GPIO) == 1:
        stop = time.time()

    elapsed = stop-start
    global fdist
    fdist = elapsed * 34300
    fdist = fdist/2
    print("Ultrasonic Measurement From Front Sensor - 1")
    print("fdist : %.1f CM" % fdist)

    # Left Corner

    GPIO.output(LEFT_CORNER_GPIO, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LEFT_CORNER_GPIO, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(LEFT_CORNER_GPIO, GPIO.LOW)
    start2 = time.time()
    GPIO.setup(LEFT_CORNER_GPIO, GPIO.IN)

    while GPIO.input(LEFT_CORNER_GPIO) == 0:
        start2 = time.time()

    while GPIO.input(LEFT_CORNER_GPIO) == 1:
        stop2 = time.time()

    elapsed2 = stop2-start2
    global ldist
    ldist = elapsed2 * 34300
    ldist = ldist/2
    print("Ultrasonic Measurement From Left Corner Sensor - 2")
    print("fdist : %.1f CM" % ldist)

    # Right Corner

    GPIO.output(RIGHT_CORNER_GPIO, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(RIGHT_CORNER_GPIO, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(RIGHT_CORNER_GPIO, GPIO.LOW)
    start = time.time()
    GPIO.setup(RIGHT_CORNER_GPIO, GPIO.IN)

    while GPIO.input(RIGHT_CORNER_GPIO) == 0:
        start3 = time.time()

    while GPIO.input(RIGHT_CORNER_GPIO) == 1:
        stop3 = time.time()

    elapsed3 = stop3-start3
    global rdist
    rdist = elapsed3 * 34300
    rdist = rdist/2
    print("Ultrasonic Measurement From Right Corner Sensor - 3")
    print("fdist : %.1f CM" % rdist)

    return fdist, ldist, rdist

def turnL():
	ser.write("S".encode())
	time.sleep(.1)
	ser.write("L".encode())
	time.sleep(1.3)
	ser.write("S".encode())
	time.sleep(.1)
	ser.write("F".encode())
	time.sleep(1.5)
	ser.write("S".encode())
	time.sleep(.1)
	ser.write("L".encode())
	time.sleep(1.4)
	ser.write("S".encode())
	time.sleep(.1)
	return

def turnR():
	print("c");
	ser.write("S".encode())
	time.sleep(.1)
	ser.write("R".encode())
	time.sleep(1.3)
	ser.write("S".encode())
	time.sleep(.1)
	ser.write("F".encode())
	time.sleep(1.5)
	ser.write("S".encode())
	time.sleep(.1)
	ser.write("R".encode())
	time.sleep(1.4)
	ser.write("S".encode())
	time.sleep(.1)
	return


if __name__ == '__main__':
	t = open("/home/ubuntu/Desktop/ECE_4961_4971_Autonomous_Crawlspace_Inspection_Robot/temp.txt", "w")
	h = open("/home/ubuntu/Desktop/ECE_4961_4971_Autonomous_Crawlspace_Inspection_Robot/hum.txt", "w")
	m = open("/home/ubuntu/Desktop/ECE_4961_4971_Autonomous_Crawlspace_Inspection_Robot/mc.txt", "w")
	loopCount = 0
	dataCount = 0
	tempRead = 0.0
	humRead = 0.0
	mcRead = 0.0
	GPIO.setmode(GPIO.BOARD)
	global cond 
	cond = True
	turn = 1; #1 means last was left, 0 means last was right
	while cond:
		#print(loopCount)
		if loopCount > 1:
			ser.write("S".encode())  
			time.sleep(.1)
			print("going")
			takePic(dataCount)
			print("gone")
			tempRead = temp.readline()
			humRead = hum.readline()
			#mcRead = mc.readline()
			mcRead = 0
			temps.append(tempRead)
			hums.append(humRead)
			mcs.append(mcRead)
			t.write(str(tempRead)+"\n")
			h.write(str(humRead)+"\n")
			m.write(str(mcRead)+"\n")
			loopCount = 0
			dataCount = dataCount + 1
		else:
			ser.write("F".encode())
			time.sleep(1)
			loopCount = loopCount + 1
			measurementInCM()
			fmain = fdist
			lmain = ldist
			rmain = rdist
			if lmain < 50 and rmain < 50:
				ser.write("B".encode())
				time.sleep(1)
				ser.write("F".encode())
				continue
			if lmain < 50:
				turnR()
				#print("Right Turn")
				turn = 0
			if rmain < 50:
				turnL()
				#print("Left Turn")
				turn = 1
			if fmain < 50:
				if turn == 1:
					turnL()
				elif turn == 0:
					turnR()
    		

