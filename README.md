# Face Mask Detection

## Project Overview
This project leverages a YOLOv8 model for detecting face masks on individuals in real-time or saved images. Using Python and OpenCV, this application identifies faces in video streams or images and classifies them into two categories: 'mask' or 'no-mask' along with a confidence score.

## Features
- Real-time face mask detection.
- Saved image face mask detection.
- Utilizes the powerful YOLOv8 model for accurate object detection.
- Includes Non-Maximum Suppression (NMS) to reduce redundant detections.

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.8 or higher
- OpenCV-Python
- TensorFlow
- PyTorch (required by YOLOv8)
- Tkinter
- Numpy
- Ultralytics
- ClearML (For training data)

Requirements can be installed using the following command: 
```pip install -r requirements.txt```

## Usage
To start the main function, run the following command:
```python main.py```

Then select the type of detection you want to do: real-time or using a saved image.

## Acknoledgements
- Thanks to the YOLOv8 team for providing an efficient and powerful object detection model.
- Thanks to OpenCV for the extensive tools that make computer vision accessible.
- Thanks to Cheng Hsun Teng for collecting the data that this model was trained on.
- Thanks to Joseph Nelson for annotating the dataset that this model was trained on.