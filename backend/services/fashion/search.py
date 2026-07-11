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


def encode_query_image(image_path):

    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    inputs = {
        k: v.to(device)
        for k, v in inputs.items()
    }

    with torch.no_grad():

        outputs = model.vision_model(**inputs)

        embedding = outputs.pooler_output

        embedding = torch.nn.functional.normalize(
            embedding,
            p=2,
            dim=1
        )

    return embedding.cpu().numpy().astype("float32")


def search_similar(
    image_path,
    gender=None,
    top_k=10
):

    query = encode_query_image(image_path)

    faiss.normalize_L2(query)

    scores, ids = index.search(
        query,
        top_k
    )

    results = []

    for score, idx in zip(scores[0], ids[0]):

        if idx == -1:
            continue

        product = metadata[idx].copy()

        # Filter products according to detected gender
        if gender is not None:
            product_gender = product.get("gender", "").strip().lower()

            if product_gender != gender.lower():
                continue

        product["image"] = f"{product['id']}.jpg"

        product["score"] = float(score)

        results.append(product)

    return results