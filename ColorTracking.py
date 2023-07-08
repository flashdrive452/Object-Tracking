import imutils
import cv2

redLower = (157, 93, 203)
redUpper = (179, 255, 255)

# using IP Camera, this 'address' points to a live camera of the USB-connected android device
address = "http://192.168.211.158:8080/video"

# initialize camera using Open-CV
camera = cv2.VideoCapture(address)

while True:
        (grabbed, frame) = camera.read()
        # Preprocess image and convert to HSV
        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # Apply mask on the area to track using HSV parameters, Remove Noise
        mask = cv2.inRange(hsv, redLower, redUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        if len(cnts) > 0:

                # Get parameters of minimum enclosing circle
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)

                # Get centre of contour area
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                if radius > 10:

                        # draw minimum enclosing circle and dot in centre
                        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        print(center, radius)

                        # Print directions based on position of dot
                        if radius > 250:
                                print("stop")
                        else:
                                if(center[0]<150):
                                        print("Left")
                                elif(center[0]>450):
                                        print("Right")
                                elif(radius<250):
                                        print("Front")
                                else:
                                        print("Stop")
        # Set key 'q' to quit
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
                break

camera.release()
cv2.destroyAllWindows()
