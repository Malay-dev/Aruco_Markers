import cv2
import cv2.aruco as aruco
import numpy as np


VideoCap = True
capture = cv2.VideoCapture(0)


def findAruco(img, marker_size=6, total_markers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{marker_size}X{marker_size}_{total_markers}')
    ARUCO_DICT = aruco.Dictionary_get(key)
    ARUCO_PARAMS = aruco.DetectorParameters_create()
    corners, ids, reject = aruco.detectMarkers(
        gray, ARUCO_DICT, parameters=ARUCO_PARAMS)
    if draw:
        aruco.drawDetectedMarkers(img, corners)
        if corners:
            corners = np.array(corners)[0]
            top_right = corners[0][1][0], corners[0][1][1]
            cv2.putText(
                img,
                f"id: {ids[0]}",
                np.array(top_right).astype(int),
                cv2.FONT_HERSHEY_PLAIN,
                1.3,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )
    return ARUCO_DICT, ARUCO_PARAMS


def pose(img, ARUCO_DICT, ARUCO_PARAMS):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, reject = aruco.detectMarkers(
        gray, ARUCO_DICT, parameters=ARUCO_PARAMS)
    if corners:
        # LOADING CAMERA CALIBRATION FILE
        calib_data_path = "Code_py/Camera Callibration/calib_data/MultiMatrix.npz"
        calib_data = np.load(calib_data_path)
        camera_matrix = calib_data["camMatrix"]
        distance_coefficient = calib_data["distCoef"]
        MARKER_SIZE = 8
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(
            corners, MARKER_SIZE, camera_matrix, distance_coefficient
        )
        for i in range(ids.size):
            cv2.drawFrameAxes(gray, camera_matrix,
                              distance_coefficient,  rVec[i], tVec[i], 4, 4)
        if corners:
            corners = np.array(corners)[0]
            bottom_right = corners[0][2][0], corners[0][2][1]
            cv2.putText(
                img,
                f"x:{round(tVec[i][0][0],1)} y: {round(tVec[i][0][1],1)} ",
                np.array(bottom_right).astype(int),
                cv2.FONT_HERSHEY_PLAIN,
                1.0,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )


while True:
    if VideoCap:
        _, frame = capture.read()
        # frame = cv2.resize(frame, (0, 0), fx=0.7, fy=0.7)
        ARUCO_DICT, ARUCO_PARAMS = findAruco(frame)
        pose(frame, ARUCO_DICT=ARUCO_DICT, ARUCO_PARAMS=ARUCO_PARAMS)
        cv2.imshow("input", frame)
        if cv2.waitKey(1) == 113:
            break
cv2.destroyAllWindows()
