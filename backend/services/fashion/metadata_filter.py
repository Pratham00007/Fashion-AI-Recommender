import pickle
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

META_PATH = PROJECT_ROOT / "indexes" / "metadata.pkl"

with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)


def filter_products(
    gender=None,
    category="Apparel",
    usage=None,
):
    filtered = []

    for idx, item in enumerate(metadata):

        if category:

            if str(item.get("masterCategory")) != category:
                continue

        if gender:

            if str(item.get("gender")) != gender:
                continue

        if usage:

            if str(item.get("usage")) != usage:
                continue

        filtered.append(
            (
                idx,
                item
            )
        )

    return filtered