import numpy as np


def body_width(mask, y):
    row = mask[y]

    pixels = np.where(row > 0)[0]

    if len(pixels) == 0:
        return 0

    return int(pixels[-1] - pixels[0])


def measure_body(mask):
    ys = np.where(mask > 0)[0]

    if len(ys) == 0:
        return None

    top = int(ys.min())
    bottom = int(ys.max())

    height = int(bottom - top)

    shoulder_y = int(top + height * 0.20)
    waist_y = int(top + height * 0.50)
    hip_y = int(top + height * 0.65)

    return {
        "height": int(height),
        "shoulderWidth": int(body_width(mask, shoulder_y)),
        "waistWidth": int(body_width(mask, waist_y)),
        "hipWidth": int(body_width(mask, hip_y)),
    }