from services.recommendation.style_rules import BODY_SHAPE_RULES
from services.recommendation.filters import valid_product


def calculate_score(product, user):

    if not valid_product(product):
        return 0

    gender = product.get("gender", "")

    if gender.lower() not in [
        user["gender"].lower(),
        "unisex"
    ]:
        return 0

    score = 50

    #######################################
    # BODY SHAPE
    #######################################

    body = BODY_SHAPE_RULES.get(
        user["bodyShape"],
        {}
    )

    sub = product.get("subCategory", "")

    article = product.get("articleType", "")

    if sub in body:
        score += body[sub].get(article, 10)

    #######################################
    # BUILD
    #######################################

    build = user["bodyProfile"]["build"]

    if build == "Slim":

        if article in [
            "Jackets",
            "Blazers",
            "Sweatshirts"
        ]:
            score += 20

    elif build == "Heavy":

        if article in [
            "Shirts",
            "Tshirts"
        ]:
            score += 20

    #######################################
    # SHOULDERS
    #######################################

    shoulders = user["bodyProfile"]["shoulders"]

    if shoulders == "Broad":

        if article in [
            "Tshirts",
            "Shirts"
        ]:
            score += 15

    elif shoulders == "Narrow":

        if article in [
            "Blazers",
            "Jackets"
        ]:
            score += 15

    #######################################
    # WAIST
    #######################################

    waist = user["bodyProfile"]["waist"]

    if waist == "Wide":

        if article in [
            "Track Pants",
            "Jeans"
        ]:
            score += 15

    elif waist == "Slim":

        if article in [
            "Trousers",
            "Jeans"
        ]:
            score += 10

    #######################################
    # Usage
    #######################################

    usage = product.get("usage", "")

    if usage == "Casual":
        score += 10

    elif usage == "Formal":
        score += 5

    return score