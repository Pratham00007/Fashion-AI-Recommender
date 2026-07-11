from services.fashion.search import search_similar


def recommend_from_image(
    image_path,
    body_features,
):

    body_shape = body_features.get(
        "bodyShape",
        "Unknown"
    )

    gender = body_features.get(
        "gender",
        None
    )

    products = search_similar(
        image_path=image_path,
        gender=gender,
        top_k=20
    )

    recommendations = []

    for p in products:

        recommendations.append({

            "id": p["id"],

            "name": p.get(
                "productDisplayName",
                ""
            ),

            "category": p.get(
                "articleType",
                ""
            ),

            "color": p.get(
                "baseColour",
                ""
            ),

            "season": p.get(
                "season",
                ""
            ),

            "usage": p.get(
                "usage",
                ""
            ),

            "image":
            f"http://127.0.0.1:8001/images/{p['id']}.jpg",

            "score": round(
                p["score"],
                3
            )

        })

    return recommendations