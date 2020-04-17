import cv2
import time

# create our first frame
first_frame = None

# create an object with the method that triggers a video capture object
# param 0 means (index 0)it will use the webcam on the computer but you put also a path
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
    # show a window
    cv2.imshow("Capturing", gray_color)

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
