import cv2
import cv2.aruco as aruco
import numpy as np


image_augment = cv2.imread("Code_py/Augumentation/1.jpg")
image_augment = cv2.resize(image_augment, (0, 0), fx=0.5, fy=0.5)

capture = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

detection = False
frame_count = 0


def augmentation(corners, img, img_augment):
    top_left = corners[0][0][0], corners[0][0][1]
    top_right = corners[0][1][0], corners[0][1][1]
    bottom_right = corners[0][2][0], corners[0][2][1]
    bottom_left = corners[0][3][0], corners[0][3][1]

    height, width, _, = img_augment.shape

    points_1 = np.array([top_left, top_right, bottom_right, bottom_left])
    points_2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrix, _ = cv2.findHomography(points_2, points_1)
    image_out = cv2.warpPerspective(
        img_augment, matrix, (img.shape[1], img.shape[0]))
    cv2.fillConvexPoly(img, points_1.astype(int), (0, 0, 0))
    image_out = img + image_out

    return image_out


def findAruco(img, marker_size=6, total_markers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{marker_size}X{marker_size}_{total_markers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParams = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(
        gray, arucoDict, parameters=arucoParams)
    if ids is not None:
        print(ids)
    return corners, ids, rejected


while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = findAruco(frame)
    if ids is not None:
        detection = True
        aruco.drawDetectedMarkers(frame, corners)
        frame = augmentation(np.array(corners)[0], frame, image_augment)
    cv2.imshow('input', frame)
    if cv2.waitKey(1) == 113:
        break
    frame_count += 1

cv2.destroyAllWindows()
