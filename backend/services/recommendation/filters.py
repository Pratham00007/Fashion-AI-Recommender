VALID_CATEGORIES = {

    "Topwear": {

        "Shirts",
        "Tshirts",
        "Sweatshirts",
        "Jackets",
        "Blazers",
        "Kurtas",
        "Sweaters",
        "Waistcoat"
    },

    "Bottomwear": {

        "Jeans",
        "Track Pants",
        "Trousers",
        "Shorts",
        "Capris",
        "Leggings"
    },

    "Dress": {

        "Dresses"
    },

    "Footwear": {

        "Casual Shoes",
        "Formal Shoes",
        "Sports Shoes",
        "Sandals",
        "Flip Flops"
    }

}


def valid_product(product):

    sub = product.get("subCategory", "")

    article = product.get("articleType", "")

    if sub not in VALID_CATEGORIES:
        return False

    return article in VALID_CATEGORIES[sub]