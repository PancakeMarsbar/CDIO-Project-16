import cv2

cap = cv2.VideoCapture('pingpong.mp4')

while True:
    _, frame = cap.read()

    table = frame[540: 735, 0: 460]
    gray_table = cv2.cvtColor(table, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_table, 195, 255, cv2.THRESH_BINARY)

    # Detect
    contour, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour:
        (x, y, w, h) = cv2.boundingRect(cnt)
        center_x = x + w/2
        center_y = y + h/2
        if w*h > 10:  # Minimum size threshold
            cv2.rectangle(table, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Show coordinates
            cv2.putText(table, f"x: {center_x}, y: {center_y}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Grayscale", gray_table)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Detected items", table)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
