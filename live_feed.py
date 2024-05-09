import cv2
from detect import detection


def get_live_feed():
    """
    Method to get the live feed from the webcam and detect faces with or without masks in real-time.
    """
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        #Detect each frame from the live feed
        detection(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break