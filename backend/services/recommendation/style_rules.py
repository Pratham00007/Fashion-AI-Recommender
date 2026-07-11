"""
Body shape styling rules.

Each body shape defines:
1. Recommended article types
2. Article types to avoid
"""

BODY_SHAPE_RULES = {

    "Rectangle": {

        "recommended": [

            "Shirts",
            "Jackets",
            "Blazers",
            "Sweatshirts",
            "Hoodies",
            "Tshirts",
            "Kurtas",
            "Waistcoat",

            "Jeans",
            "Trousers",
            "Chinos",
            "Track Pants"
        ],

        "avoid": [

            "Oversized Tshirts"
        ]
    },

    "Inverted Triangle": {

        "recommended": [

            "Jeans",
            "Track Pants",
            "Cargo Pants",
            "Trousers",

            "Polo Tshirts",
            "Simple Shirts",
            "Henley Tshirts"
        ],

        "avoid": [

            "Blazers",
            "Shoulder Jackets"
        ]
    },

    "Pear": {

        "recommended": [

            "Blazers",
            "Structured Jackets",
            "Shirts",
            "Polo Tshirts",

            "Straight Jeans",
            "Regular Trousers"
        ],

        "avoid": [

            "Skinny Jeans"
        ]
    }

}