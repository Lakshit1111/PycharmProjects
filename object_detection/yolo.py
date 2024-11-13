from ultralytics import YOLO
import cv2

model = YOLO("object_detection/model/yolov8n.pt")

data = {
    "cell phone": 0.15,  
    "person": 1.7       
}


FOCAL_LENGTH = 800 

def estimate_distance(real_height, focal_length, object_height_in_pixels):
    if object_height_in_pixels == 0:  # Avoid division by zero
        return None
    return (real_height * focal_length) / object_height_in_pixels

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    results = model(frame, conf=0.6)


    for r in results:
        boxes = r.boxes 

        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_id = int(box.cls[0])
            conf = box.conf[0] 

        
            object_name = model.names[class_id]

        
            object_height_in_pixels = y2 - y1

        
            if object_name in data:
                real_height = data[object_name]
                distance = estimate_distance(real_height, FOCAL_LENGTH, object_height_in_pixels)

                if distance is not None:
                
                    cv2.putText(frame, f"Distance: {distance:.2f} meters", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                label = f"{object_name} {int(conf * 100)}%"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("YOLO Object Detection with Distance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
