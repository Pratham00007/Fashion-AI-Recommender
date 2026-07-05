import cv2
import mediapipe as mp
from services.recommendation.body_shape import detect_body_shape
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from services.analysis.segmentation import segment_person
from services.analysis.measurement import measure_body
from services.recommendation.ai_recommender import recommend_from_image
FACE_MODEL = "models/face_landmarker.task"
POSE_MODEL = "models/pose_landmarker_lite.task"


def analyze_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return {
            "faceDetected": False,
            "bodyDetected": False,
            "bodyLandmarks": 0
        }

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    # ---------------- FACE ----------------
    face_options = vision.FaceLandmarkerOptions(
        base_options=python.BaseOptions(model_asset_path=FACE_MODEL),
        running_mode=vision.RunningMode.IMAGE
    )

    face_landmarker = vision.FaceLandmarker.create_from_options(face_options)
    face_result = face_landmarker.detect(mp_image)
    face_detected = len(face_result.face_landmarks) > 0
    face_landmarker.close()

    # ---------------- POSE ----------------
    pose_options = vision.PoseLandmarkerOptions(
        base_options=python.BaseOptions(model_asset_path=POSE_MODEL),
        running_mode=vision.RunningMode.IMAGE
    )

    pose_landmarker = vision.PoseLandmarker.create_from_options(pose_options)
    pose_result = pose_landmarker.detect(mp_image)

    body_detected = len(pose_result.pose_landmarks) > 0

    if body_detected:
        landmark_count = len(pose_result.pose_landmarks[0])
        body_shape = detect_body_shape(pose_result.pose_landmarks)
    else:
        landmark_count = 0
        body_shape = "Unknown"

    mask = segment_person(image_path)

    if mask is not None:
        measurements = measure_body(mask)
    else:
        measurements = None

    recommendations = recommend_from_image(
    image_path,
    {
        "bodyShape": body_shape,
        "measurements": measurements
    }
)

    pose_landmarker.close()

    return {
    "faceDetected": bool(face_detected),
    "bodyDetected": bool(body_detected),
    "bodyLandmarks": int(landmark_count),
    "bodyShape": str(body_shape),
    "measurements": measurements,
    "recommendations": recommendations
}