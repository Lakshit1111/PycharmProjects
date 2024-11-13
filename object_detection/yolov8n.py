from ultralytics import YOLO
import cv2
import numpy as np
import random


file = open("object_detection/data/coco.txt" , "r").read()
class_list  = file.split("\n")

detection_colour = []
for i in class_list:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    detection_colour.append((r,g,b))
# print(detection_colour)
# print(class_list)
model = YOLO("object_detection/model/yolov8n.pt" , "v8")

frame_wid = 680
frame_height = 480

cap = cv2.VideoCapture(0)

if not cap.isOpened:
    print("Cannot open camera")
    exit()

while True:
    ret,frame = cap.read()

    if not ret:
        print("Frame not captured")
        exit()

    detect_params = model.predict(source=frame , conf = 0.45 , save = False)

    boxes = []

    for r in detect_params:
        boxes.append(r.boxes.data.numpy())

    detect_params = detect_params[0].numpy()


    if len(detect_params) != 0:
        
        for param in boxes[0]:
            print("params" , param)
            top_left = (int(param[0]), int(param[1]))  # (x1, y1)
            bottom_right = (int(param[2]), int(param[3]))  # (x2, y2)
            print(top_left , bottom_right , param[5])

    

            # Draw the rectangle on the frame
            cv2.rectangle(frame, top_left, bottom_right,color= detection_colour[int(param[5])] , thickness=3)

            font = cv2.FONT_HERSHEY_COMPLEX
            # cv2.putText(frame , class_list())
    
    print("sajdoais")
        
    cv2.imshow("ObjectDection", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    