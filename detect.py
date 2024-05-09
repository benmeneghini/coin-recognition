import cv2
from ultralytics import YOLO
from preprocess import adjust_contrast
from ultralytics.utils.plotting import Annotator
import tensorflow as tf


def detection(image):
    # Preprocess and read the image from the image path.
    # image = adjust_contrast(image)

    model = YOLO('runs/detect/yolov8n_custom/weights/best.pt')
    res = model.predict(image, imgsz=640)

    for result in res:
        annotator = Annotator(image)

        boxes = result.boxes
        for box in boxes:
            box_coords = box.xyxy[0]
            cls = int(box.cls)
            conf = float(box.conf)
            print(conf)
            label = model.names[cls] + f"-{conf:.2f}"
            annotator.box_label(box_coords, label)

    image = annotator.result()
    cv2.imshow("Face Mask Detection", image)
        