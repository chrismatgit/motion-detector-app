import cv2
import time

# create our first frame
first_frame = None

# create an object with the method that triggers a video capture object
# param 0 means (index 0)it will use the webcam on the computer but you put also a path
# Using cv2.CAP_DSHOW removes the warning, but slows down my frame rate
# video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
video = cv2.VideoCapture(0)

while True:
    # "check" is used to check if the video is running or not
    # "frame" is a numpy array
    check, frame = video.read()

    # converting the frame so the color frame in a gray imag
    gray_color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # storing the first frame
    if first_frame is None:
        first_frame = gray_color
        # go to the begining of the loop
        continue
    # calculate the difference between the first frame and the current frame of the image
    delta_frame = cv2.absdiff(first_frame, gray_color)

    # implementing the treshold frame
    thresh_frame = cv2.threshold(
        delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # removing black from those big white areas in the image
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # contour detection
    # find contours method find the contours in my image and store them in a tuple
    # (_, cnts, _) = cv2.findContours(thresh_frame.copy(),
    #                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierachy = cv2.findContours(
        thresh_frame.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # if the area has less than 1000 pixels, go to the next contour
        if cv2.contourArea(contour) < 1000:
            continue
        # the draw contours method draws contours in an image
        (x, y, w, h) = cv2.boundingRect(contour)
        # draw the rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # displaying the gray frame
    cv2.imshow("Gray Frame", gray_color)
    # displaying the delta frame
    cv2.imshow("Delta Frame", delta_frame)
    # displaying the thresh_delta frame
    cv2.imshow("Threshold Frame", thresh_frame)
    # displaying the color frame
    cv2.imshow("Color Frame", frame)

    # wait time in millisecond
    key = cv2.waitKey(1)
    print(gray_color)

    # if the button key is pressed break
    if key == ord('q'):
        break

# access my object video
video.release()
# distroy a window
cv2.destroyAllWindows
