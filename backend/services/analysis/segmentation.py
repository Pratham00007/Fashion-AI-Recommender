from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolo11n-seg.pt")


def segment_person(image_path):

    results = model(image_path, verbose=False)

    if len(results) == 0:
        return None

    result = results[0]

    if result.masks is None:
        return None

    masks = result.masks.data.cpu().numpy()

    classes = result.boxes.cls.cpu().numpy()

    person_mask = None

    max_area = 0

    for i, cls in enumerate(classes):

        if int(cls) != 0:
            continue

        mask = masks[i]

        area = np.sum(mask)

        if area > max_area:
            max_area = area
            person_mask = mask

    if person_mask is None:
        return None

    image = cv2.imread(image_path)

    h, w = image.shape[:2]

    mask = cv2.resize(
        person_mask.astype(np.uint8),
        (w, h),
        interpolation=cv2.INTER_NEAREST
    )

    return mask