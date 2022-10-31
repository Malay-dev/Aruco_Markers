import cv2
import cv2.aruco as aruco
import numpy as np


VideoCap = True
cap = cv2.VideoCapture(0)


def findAruco(img, marker_size=6, total_markers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{marker_size}X{marker_size}_{total_markers}')
    ARUCO_DICT = aruco.Dictionary_get(key)
    ARUCO_PARAMS = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(
        gray, ARUCO_DICT, parameters=ARUCO_PARAMS)
    if corners:
        print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, corners)
    return corners, ids


while True:
    if VideoCap:
        _, frame = cap.read()
        corners, ids = findAruco(frame)

        cv2.imshow("input", frame)
        if cv2.waitKey(1) == 113:
            break
cv2.destroyAllWindows()
