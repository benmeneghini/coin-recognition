import cv2
from ultralytics import YOLO
from preprocess import adjust_contrast

def detection(image_path):
    # Preprocess and read the image from the image path.
    # image = adjust_contrast(image_path)

    # Read the image
    image = cv2.imread(image_path)

    model = YOLO('runs/detect/yolov8n_custom/weights/best.pt')
    res = model.predict(image_path, show=True, imgsz=640)

    # Draw bounding boxes and labels on the image
    # for *box, conf, cls in res.xyxy[0]:
    #     x1, y1, x2, y2 = map(int, box)
    #     label = model.names[int(cls)]
    #     cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #     cv2.putText(image, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Face Mask Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()