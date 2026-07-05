# AI Fashion Stylist (Work in Progress)

## Project Goal

Build a **real AI-powered fashion recommendation web application** that analyzes a user's uploaded image and recommends clothing they should wear.

The project must **NOT** use OpenAI, Gemini, or any LLM for recommendations.

Recommendations should come from:

* Computer Vision
* Pretrained AI Models
* Fashion Embeddings
* Vector Search
* Machine Learning

The final output should be actual clothing images from the dataset instead of plain text.

---

# Tech Stack

## Frontend

* React (Vite)
* Axios

## Backend

* FastAPI
* Python

## AI Models

* MediaPipe Tasks

  * Face Landmarker
  * Pose Landmarker
* YOLO11 Segmentation
* FashionCLIP (HuggingFace implementation)
* FAISS

## Image Processing

* OpenCV
* Pillow

## ML

* PyTorch
* Transformers

---

# Current Folder Structure

```
Fashion-AI/

│
├── backend/
│
│   ├── app/
│   │
│   │   └── routes/
│   │        upload.py
│   │
│   ├── services/
│   │
│   │   ├── analysis/
│   │   │
│   │   │   constants.py
│   │   │   segmentation.py
│   │   │   measurement.py
│   │   │
│   │   ├── fashion/
│   │   │
│   │   │   fashion_clip.py
│   │   │   build_index.py
│   │   │   search.py
│   │   │   metadata_filter.py
│   │   │
│   │   ├── recommendation/
│   │   │
│   │   │   body_shape.py
│   │   │   ai_recommender.py
│   │
│   ├── uploads/
│   │
│   ├── indexes/
│   │
│   │   faiss.index
│   │   embeddings.npy
│   │   metadata.pkl
│   │
│   ├── models/
│   │
│   │   face_landmarker.task
│   │   pose_landmarker_lite.task
│   │
│   ├── utils/
│   │
│   │   image_analysis.py
│   │
│   ├── main.py
│   │
│   └── requirements.txt
│
├── dataset/
│
│   └── fashion-dataset/
│
│       images/
│       styles.csv
│
└── frontend/
```

---

# Backend Completed

## FastAPI

Completed

* Image Upload API
* Static Image Serving
* Swagger
* CORS

Backend runs on

```
http://127.0.0.1:8001
```

NOT 8000.

---

# React Completed

Completed

* Image Upload
* Image Preview
* API Integration
* Analysis Display
* Recommendation Cards

---

# AI Pipeline Completed

User uploads image

↓

MediaPipe Face Detection

↓

MediaPipe Pose Detection

↓

YOLO Segmentation

↓

Body Measurements

↓

Body Shape Detection

↓

FashionCLIP Image Embedding

↓

FAISS Search

↓

React UI

---

# AI Models Used

## MediaPipe Tasks

Using

FaceLandmarker

PoseLandmarker

NOT old mediapipe.solutions API.

Current implementation uses

```
face_landmarker.task
pose_landmarker_lite.task
```

---

## YOLO

Used for

Person Segmentation

Outputs

Binary Mask

---

## FashionCLIP

IMPORTANT

The project DOES NOT use the fashion-clip pip package.

Instead it uses

```
patrickjohncyh/fashion-clip
```

loaded via

```
transformers
```

Current implementation

```
CLIPProcessor

CLIPModel

vision_model()

pooler_output
```

Embeddings are normalized before indexing.

---

## FAISS

Index built successfully.

Files

```
faiss.index

metadata.pkl

embeddings.npy
```

Dataset indexing completed.

---

# Image Analysis

Current output

```
faceDetected

bodyDetected

bodyLandmarks

bodyShape

measurements
```

measurements contains

```
height

shoulderWidth

waistWidth

hipWidth
```

---

# Recommendation Engine

Current implementation

```
recommend_from_image()

↓

search_similar()

↓

Top Products
```

Current recommendation returns

```
id

name

category

color

season

usage

image

score
```

Images are served by

```
http://127.0.0.1:8001/images/<id>.jpg
```

React displays

Product Image

Product Name

Category

Season

Usage

Score

---

# Dataset

Using

Fashion Product Images (Small)

Folder

```
dataset/

fashion-dataset/

images/

styles.csv
```

---

# Models Folder

Contains

```
models/

face_landmarker.task

pose_landmarker_lite.task
```

---

# Packages Installed

```
fastapi

uvicorn

opencv-python

numpy

pillow

mediapipe

torch

torchvision

transformers

faiss-cpu

pandas

tqdm

ultralytics

scikit-image

scipy

aiofiles
```

---

# Important Changes Already Made

The following changes were made during development and MUST NOT be reverted.

## 1

Backend uses

```
Port 8001
```

NOT

8000

---

## 2

FashionCLIP implementation

The pip package was removed.

Current implementation is custom using

```
transformers
```

with

```
patrickjohncyh/fashion-clip
```

---

## 3

build_index.py

Uses

```
Path(__file__).resolve()
```

NOT fragile ../../ paths.

Project root is calculated using pathlib.

---

## 4

image_analysis.py

Uses MediaPipe Tasks API.

DO NOT switch back to

```
mediapipe.solutions
```

---

# Current Problem

Current recommendation searches using the uploaded person image.

This causes

"similar clothing"

instead of

"best clothing".

This must be fixed.

---

# Next Phase (Highest Priority)

Build a REAL AI recommendation system.

DO NOT use

* if-else rules
* hardcoded mappings
* Gemini
* OpenAI
* rule tables

Instead build:

## Step 1

Metadata filtering

Use

styles.csv

before FAISS search.

Filter

* gender
* apparel only
* usage
* season
* articleType

Reduce search space.

---

## Step 2

FashionCLIP Text Encoder

Instead of searching with the person's image,

generate a fashion query like

```
minimal oversized streetwear
summer casual navy shirt relaxed fit
```

Encode this text using FashionCLIP's text encoder.

Search FAISS using the text embedding.

This retrieves clothes matching the desired style rather than visually similar clothes.

---

## Step 3

Hybrid Ranking

Final score should combine

* FashionCLIP similarity
* Body measurements
* Body shape
* Metadata
* Season
* Occasion
* Color compatibility

instead of raw cosine similarity.

---

## Step 4

Outfit Generator

Instead of individual items,

recommend complete outfits.

Example

Top

Bottom

Shoes

Watch

Accessories

---

## Step 5

Modern UI

Redesign React.

Need

* Hero Section
* Drag & Drop Upload
* Loading Animation
* AI Analysis Panel
* Recommendation Grid
* Product Details Modal
* Responsive Design
* Dark Mode

---

## Step 6

Optional Future Improvements

* Skin Tone Detection
* Face Shape Detection
* Hair Color Detection
* Gender Detection
* Age Estimation
* Occasion Selection
* Weather API
* Wishlist
* Similar Outfit Search
* Virtual Try-On
* Multi-image recommendations

---

# Instructions For Continuing In A New Chat

Continue this project from the current state without recreating previous files.

Assume all existing modules work unless I explicitly report an error.

When generating code:

* Always provide the exact file path.
* Give complete code for each file.
* Use the existing project architecture.
* Do not replace working code unnecessarily.
* Keep using FastAPI + React + MediaPipe Tasks + YOLO + FashionCLIP + FAISS.
* Prefer production-quality implementations over demo code.
* Continue building from the "Next Phase" section above until the project is complete.
