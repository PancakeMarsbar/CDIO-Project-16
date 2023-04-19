import cv2
import numpy as np

# Define the callback function for mouse events
def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Calculate the average BGR value of pixels within a 10 pixel radius
        mask = np.zeros_like(frame)
        cv2.circle(mask, (x, y), 10, (255, 255, 255), -1)
        masked_image = cv2.bitwise_and(frame, mask)
        num_pixels = np.count_nonzero(mask[:, :, 0])
        bgr_avg = np.sum(masked_image, axis=(0, 1)) / num_pixels
        print(f"Clicked on pixel ({x}, {y}): BGR average = {bgr_avg}")

# Open a connection to the default webcam
cap = cv2.VideoCapture(0)

# Create a window to display the webcam feed and set the mouse callback function
cv2.namedWindow("webcam feed")
cv2.setMouseCallback("webcam feed", on_mouse_click)

# Loop over frames from the webcam feed
while True:
    # Read a frame from the webcam feed
    ret, frame = cap.read()

    # Display the frame and wait for a key press
    cv2.imshow("webcam feed", frame)
    key = cv2.waitKey(1) & 0xFF

    # Check for the 'q' key to exit the loop
    if key == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
