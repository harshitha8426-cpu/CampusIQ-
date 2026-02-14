# CampusIQ – AI-Powered Smart Campus Living Lab

## 🚀 Overview

CampusIQ transforms a college campus into a real-time AI-driven Living Lab that models scalable smart city solutions.

It integrates computer vision, predictive analytics, and IoT-based data simulation to optimize mobility, infrastructure health, and resource utilization.

---

## 🎯 Problem Statement

Campuses operate like small cities but lack unified, predictive intelligence systems.
This leads to congestion, inefficient waste management, underutilized spaces, and reactive maintenance.

---

## 💡 Solution

CampusIQ provides a unified AI intelligence layer that:

- Detects crowd density using YOLOv8
- Predicts congestion and infrastructure risks
- Forecasts waste overflow
- Provides real-time actionable insights

---

## 🧠 Key Features

- AI-Based Crowd Detection
- Predictive Risk Engine
- Smart Resource Optimization
- Real-Time Command Dashboard
- Scalable Smart-City Architecture

---

## 🏗 Architecture

Data Sources → Edge AI → ML Prediction → API Layer → Dashboard → Administrative Action

---

## 🛠 Tech Stack

- Python
- FastAPI
- YOLOv8 (Ultralytics)
- Scikit-learn
- Streamlit
- Docker
- AMD Ryzen / Radeon Acceleration

---

## ⚙ Setup Instructions

### Install dependencies
pip install -r requirements.txt

### Train model
python backend/app/models/train_model.py

### Run backend
uvicorn backend.app.main:app --reload

### Run dashboard
streamlit run frontend/dashboard.py

---

## 🌍 Impact

- Reduced congestion
- Lower operational cost
- Predictive maintenance
- Scalable smart-city blueprint

---

## ⚡ AMD Utilization

CampusIQ leverages AMD multi-core processing and GPU acceleration for real-time AI inference and scalable analytics workloads.
