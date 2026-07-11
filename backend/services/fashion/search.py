import pickle
from pathlib import Path

import faiss
import numpy as np
from PIL import Image

from services.fashion.fashion_clip import processor, model, device
import torch


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INDEX_PATH = PROJECT_ROOT / "indexes" / "faiss.index"
META_PATH = PROJECT_ROOT / "indexes" / "metadata.pkl"


index = faiss.read_index(str(INDEX_PATH))

with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)

from services.recommendation.scorer import calculate_score


def search_similar(
        image_path,
        gender,
        body_shape,
        body_profile,
        top_k=20
):

    user = {

        "gender": gender,

        "bodyShape": body_shape,

        "bodyProfile": body_profile

    }

    ranked = []

    for product in metadata:

        score = calculate_score(
            product,
            user
        )

        if score <= 0:
            continue

        p = product.copy()

        p["score"] = score

        p["image"] = f"{p['id']}.jpg"

        ranked.append(p)

    ranked = sorted(

        ranked,

        key=lambda x: x["score"],

        reverse=True

    )

    return ranked[:top_k]