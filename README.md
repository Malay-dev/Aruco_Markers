# Aruco_Markers

Generate_aruco.py
This code will generate aruco markers according to the given aruco_type and id
For aruco_type = "DICT_5X5_250" and id = 43
![image](https://user-images.githubusercontent.com/91375797/199019606-8418fdf0-7dde-4406-a9da-182bf60e4220.png)

Detect_aruco.py

```python
aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAMS)
```

This function returns the corners and id of the detected marker according to the aruco dictionary and the parameters

```python
aruco.drawDetectedMarkers(img, corners)
```

This function draws a bounding box around the detected marker by using the corner co-ordinates

Distance_Estimation.py and Pose_Estimation.py
For accurate distance estimation and pose estimation we need to calibrate camera and use its data - Camera matrix, distance coefficient to calculate the distance

This function returns the required vectors rVec and tVec to estimate pose and distance respectivily
rVec - rotation vector
tVec - translation vector

```python
rVec, tVec, _ = aruco.estimatePoseSingleMarkers(
            corners, MARKER_SIZE, camera_matrix, distance_coefficient
        )
for i in range(ids.size):
    distance = np.sqrt(
        tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
    )
```

This function receives the detected markers and returns their pose estimation respect to the camera individually. So for each marker, one rotation and translation vector is returned. The returned transformation is the one that transforms points from each marker coordinate system to the camera coordinate system. The marker coordinate system is centered on the middle (by default) or on the top-left corner of the marker, with the Z axis perpendicular to the marker plane. estimateParameters defines the coordinates of the four corners of the marker in its own coordinate system (by default) are: (-markerLength/2, markerLength/2, 0), (markerLength/2, markerLength/2, 0), (markerLength/2, -markerLength/2, 0), (-markerLength/2, -markerLength/2, 0)

```python
for i in range(ids.size):
            cv2.drawFrameAxes(gray, camera_matrix,
                              distance_coefficient,  rVec[i], tVec[i], 4, 4)

```

to draw the axes on the frame
