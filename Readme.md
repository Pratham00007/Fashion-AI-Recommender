# AI Fashion Stylist

A modern, AI-powered fashion recommendation web application that analyzes a person's body features from a full-body image and recommends clothing that suits them—not based on what they are already wearing, but based on their body profile.

---
## Video



https://github.com/user-attachments/assets/a449ab8f-91cb-4779-b211-a6253b8ed647



---
## Features

* Full-body image upload
* Body shape detection using MediaPipe
* Person segmentation using YOLO
* Automatic body measurement extraction
* Gender detection
* Body profile generation
* AI-based clothing recommendation
* Interactive React frontend
* FastAPI backend
* Responsive recommendation cards with clothing images

---

## Tech Stack

### Frontend

* React (Vite)
* Axios
* HTML
* CSS
* JavaScript

### Backend

* FastAPI
* Python
* Uvicorn

### AI & Computer Vision

* MediaPipe Tasks
* YOLOv11
* OpenCV
* DeepFace

### Machine Learning

* PyTorch
* Transformers
* FashionCLIP
* FAISS

### Dataset

* Fashion Product Images (Small)

---

# Project Architecture

```text
                        Upload Image
                              │
                              ▼
                   Face Detection (MediaPipe)
                              │
                              ▼
                  Gender Detection (DeepFace)
                              │
                              ▼
                  Pose Detection (MediaPipe)
                              │
                              ▼
                  Person Segmentation (YOLO)
                              │
                              ▼
                 Body Measurement Extraction
                              │
                              ▼
                   Body Shape Identification
                              │
                              ▼
                  Body Profile Generation
                              │
                              ▼
                Recommendation Engine
                              │
                              ▼
              Clothing Recommendation Results
                              │
                              ▼
                    React Web Interface
```

---

# Project Structure

```text
Fashion-AI/
│
├── backend/
│   │
│   ├── app/
│   │   └── routes/
│   │       └── upload.py
│   │
│   ├── services/
│   │   │
│   │   ├── analysis/
│   │   │   ├── segmentation.py
│   │   │   ├── measurement.py
│   │   │   ├── gender.py
│   │   │   └── constants.py
│   │   │
│   │   ├── fashion/
│   │   │   ├── fashion_clip.py
│   │   │   ├── build_index.py
│   │   │   ├── metadata_filter.py
│   │   │   └── search.py
│   │   │
│   │   └── recommendation/
│   │       ├── ai_recommender.py
│   │       ├── body_shape.py
│   │       ├── body_profile.py
│   │       ├── style_rules.py
│   │       ├── scorer.py
│   │       └── filters.py
│   │
│   ├── uploads/
│   ├── indexes/
│   │   ├── faiss.index
│   │   ├── embeddings.npy
│   │   └── metadata.pkl
│   │
│   ├── models/
│   │   ├── face_landmarker.task
│   │   └── pose_landmarker_lite.task
│   │
│   ├── utils/
│   │   └── image_analysis.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── dataset/
│   └── fashion-dataset/
│       ├── images/
│       └── styles.csv
│
├── frontend/
│
└── README.md
```

---

# Dataset

This project uses the **Fashion Product Images (Small)** dataset.

Dataset contains

* Product Images
* Clothing Metadata
* Gender
* Category
* Article Type
* Season
* Usage
* Product Name

Example

```csv
id,gender,masterCategory,subCategory,articleType,baseColour,season,usage
15970,Men,Apparel,Topwear,Shirts,Navy Blue,Fall,Casual
```

---

# Download Dataset

Download the dataset from Kaggle:

[https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small)

Extract it inside

```text
dataset/
    fashion-dataset/
```

Final structure

```text
dataset/

    fashion-dataset/

        images/

        styles.csv
```

---

# Download MediaPipe Models

Download these two MediaPipe Task models.

### Face Landmarker

[https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task](https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task)

### Pose Landmarker Lite

[https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task](https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task)

Place them inside

```text
backend/models/
```

---

# Backend Requirements

Create

```text
backend/requirements.txt
```

```text
fastapi
uvicorn
python-multipart
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
deepface
tensorflow
tf-keras
```

Install packages

```bash
pip install -r requirements.txt
```

---

# Frontend Dependencies

```bash
npm install
```

---

# Run Backend

Open terminal

```bash
cd backend
```

Activate virtual environment

```bash
venv\Scripts\activate
```

Run FastAPI

```bash
uvicorn main:app --reload --port 8001
```

Backend URL

```text
http://127.0.0.1:8001
```

Swagger Documentation

```text
http://127.0.0.1:8001/docs
```

---

# Run Frontend

Open another terminal

```bash
cd frontend
```

Start React

```bash
npm run dev
```

Frontend URL

```text
http://localhost:5173
```

---

# AI Pipeline

```text
                  User Uploads Image
                           │
                           ▼
                 Face Detection (MediaPipe)
                           │
                           ▼
               Gender Detection (DeepFace)
                           │
                           ▼
                Pose Detection (MediaPipe)
                           │
                           ▼
               Person Segmentation (YOLO)
                           │
                           ▼
               Body Measurement Extraction
                           │
                           ▼
                 Body Shape Detection
                           │
                           ▼
                 Body Profile Generation
                           │
                           ▼
                Recommendation Engine
                           │
                           ▼
                Top Clothing Suggestions
```

---

# Current Recommendation Strategy

The recommendation engine considers

* Gender
* Body Shape
* Body Measurements
* Body Profile
* Clothing Category
* Clothing Type
* Usage
* Season

The goal is to recommend clothing suitable for the user rather than matching the clothes already worn in the uploaded image.

---

# API Endpoint

## Upload Image

```http
POST /upload
```

Response

```json
{
  "faceDetected": true,
  "bodyDetected": true,
  "gender": "Men",
  "bodyShape": "Rectangle",
  "bodyProfile": {
    "build": "Average",
    "shoulders": "Broad",
    "waist": "Average",
    "hips": "Normal"
  },
  "measurements": {
    "height": 672,
    "shoulderWidth": 238,
    "waistWidth": 214,
    "hipWidth": 227
  },
  "recommendations": [
    {
      "id": 15970,
      "name": "Turtle Check Men Navy Blue Shirt",
      "category": "Shirts",
      "score": 165
    }
  ]
}
```

---

# Future Improvements

* Skin tone detection
* Weather-aware recommendations
* Occasion-based styling (Casual, Formal, Party, Gym)
* Complete outfit generation (Top + Bottom + Footwear)
* Color harmony analysis
* Accessory recommendations
* Personalized wardrobe creation
* User preference learning
* Recommendation history
* Favorite outfits
* AI stylist chatbot

---

# Author

**Pratyaksh Khetrapal**


---

⭐ If you found this project useful, consider giving it a star on GitHub.
