# Gesture_Pattern_detection_Model
Simple Python code to track the gesture of movement in front of camera and display the movement pattern.
<br>
<br>
To run this code you must be sure that you have open cv installed on your system.
<br>
I would recommend installing opencv version 4.2.0 because the MOSSE tracker tends to not function in other versions.
To install the specefic version of opencv in cmd type `pip install opencv-contrib-python==4.2.0`.
<br>
<br>
NOTE:: This code uses open cv version 4.2.0  .
<br>
<br>
So make sure you have it installed. To install python and pip from ground level go to end of this file.
<br>
<br>
This code uses cv2 and its MOSSE tracker and matplotlib to plot the gesture pattern.
```
cap = cv2.VideoCapture(0)
```
Using front camera to capture gestures.
```
tracker = cv2.TrackerMOSSE_create()
```
Creating a MOSSE tracker.
```
def drawbox(img, bbox):
   .......
   x_coord.append(x)
	 y_coord.append(y)
   ````
Defining the function drawbox which is used to draw the box to identify the object to be tracked.
Inside the function we update two arrays which store the values of x and y coordinates.
```
def graph_plot():
```
In this function we use matplotlib's `plot()` function to plot the x and y cordinates.
```
if cv2.waitKey(1) & 0xff == ord('q'):
```
The tracking stops as we press 'q' button on our keyboard.
<br>
<br>
#### To freshly install python and pip::
First check if you have python installed in your computer.
Open command prompt and type the command `python --version`.
<br>
<br>
If version does not appears that means your system does not have python installed properly.
Head over to `python.org` and download and install python first.
While installing be sure to check the `Add python to PATH` button.
<br>
<br>
To check the successful installation of python, in cmd type `python --version`. If the version appears, then it is installed.
Newer versions of python have pip preinstalled by defult.
<br>
<br>
If python is installed then type `pip`, if it executes properly then pip is present in your system.
You should be good to go now.
