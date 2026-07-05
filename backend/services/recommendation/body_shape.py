import math


LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12

LEFT_HIP = 23
RIGHT_HIP = 24


def distance(a, b):
    return math.sqrt(
        (a.x - b.x) ** 2 +
        (a.y - b.y) ** 2
    )


def detect_body_shape(landmarks):

    if landmarks is None or len(landmarks) == 0:
        return "Unknown"

    pose = landmarks[0]

    shoulder = distance(
        pose[LEFT_SHOULDER],
        pose[RIGHT_SHOULDER]
    )

    hip = distance(
        pose[LEFT_HIP],
        pose[RIGHT_HIP]
    )

    ratio = shoulder / hip

    if ratio > 1.15:
        return "Inverted Triangle"

    elif ratio < 0.85:
        return "Pear"

    else:
        return "Rectangle"