from deepface import DeepFace


def detect_gender(image_path):
    """
    Detect gender from uploaded image.

    Returns:
        Men
        Women
    """

    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=["gender"],
            enforce_detection=False,
            silent=True
        )

        if isinstance(result, list):
            result = result[0]

        gender = result["dominant_gender"]

        if gender.lower() == "man":
            return "Men"

        return "Women"

    except Exception as e:
        print("Gender Detection Error:", e)
        return None