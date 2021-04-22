import cv2

import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)


tracker = cv2.TrackerMOSSE_create()
success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)


x_coord = []
y_coord = []

def drawbox(img, bbox):
	x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
	cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255,0,255), 3, 1)
	#Format cv2.rectangle(image, start_coord, end_coord, colour, thickness)
	cv2.putText(img, "Tracking", (50,130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,225,0), 1)

	x_coord.append(x)
	y_coord.append(y)


def graph_plot():
	plt.plot(x_coord, y_coord, 'ro') #ro means red circle
	plt.gca().invert_yaxis()
	plt.axis('equal')
	plt.show()

while True:
	timer = cv2.getTickCount()
	success, img = cap.read()
	print(bbox) #it is a tuple FORMAT(x coord, y coord, width, height)

	success, bbox = tracker.update(img)

	if success is True:
		drawbox(img, bbox)
		
	else:
		cv2.putText(img, "Lost", (50,130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,225), 1)


	fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
	cv2.putText(img, str(int(fps)), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,225), 1)
	#FORMAT IS (window_name, what to display, coordinates, font, scale, colour, thickness)
	cv2.imshow("Tracking", img)

	if cv2.waitKey(1) & 0xff == ord('q'): #key to stop camera / tracking
		graph_plot()
		break