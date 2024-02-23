from ultralytics import YOLO
import cv2
import numpy as np

# Load a pretrained YOLOv8n model
model = YOLO('yolov8x.pt')

img = "test.jpg"
img = cv2.imread(img)

# Run inference on image
results = model(img)  # results list

# View results
for r in results:
    # Initiating a list for the detected classes for r in results
    for box, c in zip(r.boxes.xyxy, r.boxes.cls):
        class_name = model.names[int(c)]
        if class_name == "person":
            x1, y1, x2, y2 = map(int, box)
            # Draw bounding boxes and labels
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)

# Show the image with bounding boxes for "person" class
cv2.imshow('YOLOv8x Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
