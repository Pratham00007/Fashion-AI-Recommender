import os
import pickle

import faiss
import numpy as np
import pandas as pd

from tqdm import tqdm

from services.fashion.fashion_clip import fclip



from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CSV_PATH = PROJECT_ROOT / "dataset/fashion-dataset/styles.csv"
IMAGE_FOLDER = PROJECT_ROOT / "dataset/fashion-dataset/images"


styles = pd.read_csv(
    CSV_PATH,
    on_bad_lines="skip"
)

embeddings = []

metadata = []

image_paths = []

for _, row in tqdm(styles.iterrows(), total=len(styles)):

    image_id = str(row["id"]) + ".jpg"

    path = os.path.join(
        IMAGE_FOLDER,
        image_id
    )

    if not os.path.exists(path):
        continue

    image_paths.append(path)

    metadata.append(row.to_dict())

vectors = fclip.encode_images(image_paths)

vectors = np.array(vectors).astype("float32")

dimension = vectors.shape[1]

index = faiss.IndexFlatIP(dimension)

faiss.normalize_L2(vectors)

index.add(vectors)

os.makedirs("indexes", exist_ok=True)

faiss.write_index(
    index,
    "indexes/faiss.index"
)

np.save(
    "indexes/embeddings.npy",
    vectors
)

with open(
    "indexes/metadata.pkl",
    "wb"
) as f:

    pickle.dump(
        metadata,
        f
    )

print("Finished.")