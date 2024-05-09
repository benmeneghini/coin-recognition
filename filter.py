import numpy as np


def non_maximum_suppression(boxes, scores, classes, iou_threshold):
    """
    Non-Maximum Suppression algorithm to filter out overlapping boxes.
    """
    unique_classes = np.unique(classes)
    selected_boxes = []
    selected_scores = []
    selected_classes = []

    for cls in unique_classes:
        # Find indices of all boxes that belong to the current class
        indices = np.where(classes == cls)[0]
        cls_boxes = boxes[indices]
        cls_scores = scores[indices]

        sorted_indices = np.argsort(cls_scores)

        while len(sorted_indices) > 0:
            last = len(sorted_indices) - 1
            best_index = sorted_indices[-1]
            selected_boxes.append(cls_boxes[best_index])
            selected_scores.append(cls_scores[best_index])
            selected_classes.append(cls)

            suppress = [last]
            for index in range(0, last):
                j = sorted_indices[index]

                # Suppress the box if it's IoU with the best box is greater than the given threshold.
                if compute_iou(cls_boxes[best_index], cls_boxes[j]) > iou_threshold:
                    suppress.append(index)

            sorted_indices = np.delete(sorted_indices, suppress)

    return np.array(selected_boxes), np.array(selected_scores), np.array(selected_classes)


def compute_iou(boxA, boxB):
    """
    Compute the Intersection over Union (IoU) of two bounding boxes.
    """
    # Coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # Area of intersection
    interArea = max(0, xB - xA) * max(0, yB - yA)

    # Area of both rectangles
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    # Interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou
