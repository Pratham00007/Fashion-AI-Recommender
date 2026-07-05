from PIL import Image
import torch
from transformers import CLIPModel, CLIPProcessor

MODEL_NAME = "patrickjohncyh/fashion-clip"

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = CLIPProcessor.from_pretrained(MODEL_NAME)
model = CLIPModel.from_pretrained(MODEL_NAME).to(device)
model.eval()


class FashionClip:

    def encode_images(self, image_paths, batch_size=32):

        embeddings = []

        for i in range(0, len(image_paths), batch_size):

            batch_paths = image_paths[i:i + batch_size]

            images = [
                Image.open(path).convert("RGB")
                for path in batch_paths
            ]

            inputs = processor(
                images=images,
                return_tensors="pt"
            )

            # move tensors to device
            inputs = {k: v.to(device) for k, v in inputs.items()}

            with torch.no_grad():

                # ✅ IMPORTANT FIX: use vision_model instead
                vision_outputs = model.vision_model(**inputs)

                features = vision_outputs.pooler_output

                features = torch.nn.functional.normalize(
                    features,
                    p=2,
                    dim=1
                )

            embeddings.append(features.cpu())

        return torch.cat(embeddings).numpy()


fclip = FashionClip()