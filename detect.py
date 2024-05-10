import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
from filter import non_maximum_suppression
import numpy as np

def detection(image):
    """
    Detection method that uses the YOLO model to detect faces with or without masks.
    Applies Non-Maximum Suppression to filter out overlapping boxes.
    """
    model = YOLO('runs/detect/yolov8n_custom/weights/best.pt')
    res = model.predict(image, imgsz=640)

    annotator = Annotator(image)
    boxes = []
    scores = []
    classes = []

    for result in res:
        for box in result.boxes:
            box_coords = box.xyxy[0].numpy()  # Convert to numpy array
            cls = int(box.cls)
            conf = float(box.conf)
            boxes.append(box_coords)
            scores.append(conf)
            classes.append(cls)

    # Applying Non-Maximum Suppression
    iou_threshold = 0.5 # Intersection over Union threshold
    boxes = np.array(boxes)
    scores = np.array(scores)
    classes = np.array(classes)
    filtered_boxes, filtered_scores, filtered_classes = non_maximum_suppression(boxes, scores, classes, iou_threshold)

    for i, box_coords in enumerate(filtered_boxes):
        conf = filtered_scores[i]
        cls = filtered_classes[i]
        label = model.names[cls] + f"-{conf:.2f}"
        annotator.box_label(box_coords, label, color=(255, 0, 0) if cls == 0 else (0, 0, 255))

    image = annotator.result()
    cv2.imshow("Face Mask Detection", image)
        