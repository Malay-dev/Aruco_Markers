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
