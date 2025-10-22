# Docker

# 🚀 NLP Sentiment Analysis API — FastAPI + Docker + Transformers

A lightweight **NLP REST API** for sentiment analysis built with **FastAPI**, **Hugging Face Transformers**, and fully containerized using **Docker**.  
This project demonstrates how to serve a transformer model as an API with a clean, step-by-step Docker workflow.

---

## ✨ Overview

- **Framework:** FastAPI  
- **Model:** `distilbert-base-uncased-finetuned-sst-2-english`  
- **Server:** Uvicorn (ASGI)  
- **Runtime:** Python 3.11 (Slim)  
- **Deployment:** Docker container  

---

## 🧱 Folder Structure

nlp-docker-demo/
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md


---

## ⚙️ 1. Build the Docker Image

```bash
docker build -t nlp-demo:0.1 .
What happens:

Docker downloads python:3.11-slim base image

Installs Python dependencies

Copies your source code into /app

Exposes port 8000

Sets the container entrypoint to run Uvicorn

🐳 2. Run the Container

docker run --rm -p 8000:8000 nlp-demo:0.1
Output should include:


INFO:     Uvicorn running on http://0.0.0.0:8000
Access it on your browser:
👉 http://localhost:8000

🔍 3. Test the API
Health Check

curl http://localhost:8000/health
Expected:

json
Copy code
{"status":"ok"}
Sentiment Analysis

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love learning Docker!"}'
Response:

{"input":"I love learning Docker!","prediction":{"label":"POSITIVE","score":0.9992}}
🌌 4. Extended Test Example
Try a longer, positive input:

“The universe is an astonishing masterpiece of beauty and order, where every star, planet, and atom moves in perfect harmony, reminding us how extraordinary it is to be alive and conscious within such a vast, mysterious, and magnificent cosmos.”

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"The universe is an astonishing masterpiece of beauty and order, where every star, planet, and atom moves in perfect harmony, reminding us how extraordinary it is to be alive and conscious within such a vast, mysterious, and magnificent cosmos."}'
🧰 5. Developer Mode (Auto Reload)
For live code editing:


docker run --rm -p 8000:8000 \
  --mount type=bind,source="$(pwd)",target=/app \
  nlp-demo:0.1 \
  uvicorn app:api --host 0.0.0.0 --port 8000 --reload
In PowerShell, replace $(pwd) with ${PWD} or a full path.

📜 6. API Documentation
FastAPI provides built-in documentation:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

⚡ 7. Pre-Caching the Model (Optional)
You can bake the model inside the Docker image to avoid downloading at runtime:


# Add inside Dockerfile (before CMD)
RUN python - <<'PY'
from transformers import pipeline
pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print("Model cached successfully.")

🚀 8. Run in Detached (Background) Mode

docker run -d --name nlp-api -p 8000:8000 nlp-demo:0.1
docker logs -f nlp-api
docker stop nlp-api && docker rm nlp-api

🧩 9. Tag & Push Image to Docker Hub 
bash

docker login
docker tag nlp-demo:0.1 yourusername/nlp-demo:0.1
docker push yourusername/nlp-demo:0.1





💬 Author
Laman Qasimli
AI Engineer • Deep Learning • NLP
📧 leman.qasimli25@aiacademy.az

🪶 “Build once, run anywhere — Docker makes machine learning deployment elegant, fast, and reproducible.”








