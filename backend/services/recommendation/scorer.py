from services.recommendation.style_rules import BODY_SHAPE_RULES


def calculate_score(product, user):

    score = 0

    #############################
    # Gender
    #############################

    if product.get("gender", "").lower() == user["gender"].lower():
        score += 50
    else:
        return 0

    #############################
    # Body Shape
    #############################

    body_shape = user["bodyShape"]

    rules = BODY_SHAPE_RULES.get(body_shape)

    if rules is None:
        return score

    article = product.get("articleType", "")

    sub = product.get("subCategory", "")

    if sub in rules["recommended"]:

        if article in rules["recommended"][sub]:
            score += 40

    #############################
    # Usage
    #############################

    usage = product.get("usage", "")

    if usage in [
        "Casual",
        "Ethnic",
        "Formal"
    ]:
        score += 5

    #############################
    # Season
    #############################

    if product.get("season") != "":
        score += 5

    return score