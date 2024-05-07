import cv2
from ultralytics import YOLO

def recognise(image_path):
    image = cv2.imread(image_path)

    model = YOLO('runs/detect/yolov8n_custom/weights/best.pt')
    res = model.predict(image_path, show=True, imgsz=640)

    pass