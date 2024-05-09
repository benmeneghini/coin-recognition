import cv2
from ultralytics import YOLO
from preprocess import adjust_contrast
from ultralytics.utils.plotting import Annotator


def detection(image):
    # Preprocess and read the image from the image path.
    # image = adjust_contrast(image_path)

    model = YOLO('runs/detect/yolov8n_custom/weights/best.pt')
    res = model.predict(image, imgsz=640)

    for result in res:
        annotator = Annotator(image)

        boxes = result.boxes
        for box in boxes:
            box_coords = box.xyxy[0]
            cls = box.cls
            annotator.box_label(box_coords, model.names[int(cls)])

    image = annotator.result()
    cv2.imshow("Face Mask Detection", image)
        