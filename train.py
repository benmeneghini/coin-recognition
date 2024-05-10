from ultralytics import YOLO


def train_model():
    """
    Method to train the YOLO model with the provided data and save the trained model.
    """

    # Load a model
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

    # Can add augmentation parameters here to improve model accuracy
    results = model.train(data='faces_v8.yaml', imgsz=640, epochs=30, name='yolov8n_custom')

train_model()