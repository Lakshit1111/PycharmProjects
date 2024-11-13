from ultralytics import YOLO
import cv2
import numpy

model = YOLO("object_detection/model/yolov8n.pt" , "v8")

detect_params = model.predict(0, conf = 0.25 , save_dir = True)

# print(detect_params)

for r in detect_params:
        print(r.boxes.data.numpy()[0])
print("shfoshshfsdfskfsfsufwiuefwuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu                 woeiiiiiiiiiiiiiiiii")
# print(prediction[0].numpy())
