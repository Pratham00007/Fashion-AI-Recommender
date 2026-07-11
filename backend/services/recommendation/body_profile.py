def build_body_profile(measurements):

    if measurements is None:
        return {
            "build": "Average",
            "shoulders": "Average",
            "waist": "Average"
        }

    shoulder = measurements["shoulderWidth"]
    waist = measurements["waistWidth"]
    hip = measurements["hipWidth"]
    height = measurements["height"]

    shoulder_ratio = shoulder / height
    waist_ratio = waist / height
    hip_ratio = hip / height

    profile = {}

    ###########################################
    # BODY BUILD
    ###########################################

    body_ratio = (shoulder + waist + hip) / (3 * height)

    if body_ratio < 0.28:
        profile["build"] = "Slim"

    elif body_ratio < 0.36:
        profile["build"] = "Average"

    else:
        profile["build"] = "Heavy"

    ###########################################
    # SHOULDERS
    ###########################################

    if shoulder_ratio > 0.34:
        profile["shoulders"] = "Broad"

    elif shoulder_ratio < 0.25:
        profile["shoulders"] = "Narrow"

    else:
        profile["shoulders"] = "Average"

    ###########################################
    # WAIST
    ###########################################

    if waist_ratio > 0.30:
        profile["waist"] = "Wide"

    elif waist_ratio < 0.20:
        profile["waist"] = "Slim"

    else:
        profile["waist"] = "Average"

    ###########################################
    # HIPS
    ###########################################

    if hip_ratio > 0.34:
        profile["hips"] = "Wide"

    else:
        profile["hips"] = "Normal"

    return profile