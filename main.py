import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # white
    diferance = 25
    lower_white = np.array([0, 0, 255 - diferance])
    upper_white = np.array([255, diferance, 255])

    # red
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])


    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # mask for colour
    mask_white = cv.inRange(hsv, lower_white, upper_white)

    mask_red = cv.inRange(hsv, lower_red, upper_red)

    test = np.where(mask_red)


    # The black region in the mask has the value of 0,
    # so when multiplied with original image removes all non-blue regions

    result = cv.bitwise_and(frame, frame, mask=(mask_red + mask_white))

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    cv.imshow('mask Red', mask_red)
    cv.imshow('mask White', mask_white)
    cv.imshow('result', result)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
