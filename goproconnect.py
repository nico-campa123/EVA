#conectar gopro a wifi
#conseguir con VLC el url del stream

import cv2

stream_url = "http://10.5.5.9:8080/live/amba.m3u8"

cap = cv2.VideoCapture(stream_url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    cv2.imshow("GoPro Live Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
