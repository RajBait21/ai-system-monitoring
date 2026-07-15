# 🚀 AI Real-Time System Monitoring Dashboard

A real-time AI-powered system monitoring application that collects system metrics, predicts system risk using Machine Learning, and displays everything on an interactive Streamlit dashboard.

## 📌 Features

- ✅ Real-time CPU Usage Monitoring
- ✅ Real-time Memory Usage Monitoring
- ✅ Real-time Disk Usage Monitoring
- ✅ AI-based Risk Prediction
- ✅ FastAPI Backend
- ✅ Streamlit Interactive Dashboard
- ✅ Docker Support
- ✅ Render Deployment
- ✅ Mobile Friendly Dashboard

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- Uvicorn
- Psutil
- Scikit-Learn
- Joblib

### Frontend
- Streamlit
- Plotly

### Deployment
- Docker
- Render
- GitHub

---

## 📂 Project Structure

```
ai-system-monitoring/
│
├── app/
│   ├── main.py
│   ├── model.pkl
│   └── scaler.pkl
│
├── dashboard/
│   └── dashboard.py
│
├── ml/
│   ├── train_model.py
│   └── generate_dataset.py
│
├── data/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/RajBait21/ai-system-monitoring.git
```

```bash
cd ai-system-monitoring
```

---

### Create Virtual Environment

Mac/Linux

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

Activate

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

Dashboard

```
http://localhost:8501
```

---

## 🐳 Docker

Build

```bash
docker build -t ai-monitor .
```

Run

```bash
docker run -p 8000:8000 ai-monitor
```

---

## 🌐 Deployment

### Backend

Deployed on Render using Docker.

### Dashboard

Deployed separately on Render using Streamlit and Docker.

---

## 📊 Dashboard

The dashboard displays:

- CPU Usage
- Memory Usage
- Disk Usage
- Predicted Risk
- Live Monitoring
- Interactive Charts

---

## 🤖 Machine Learning Model

Model Used:

- Random Forest Classifier

Features:

- CPU Usage
- Memory Usage
- Disk Usage

Output:

- Normal
- Warning
- Critical

## 👨‍💻 Author

**Raj Bait**

AI & Data Science Engineering Student

GitHub:
https://github.com/RajBait21

---

## ⭐ Future Improvements

- Email Alerts
- SMS Notifications
- Kubernetes Monitoring
- GPU Monitoring
- Multi-Server Monitoring
- Cloud Deployment
- Authentication
- Historical Analytics

---

## 📄 License

This project is developed for educational and learning purposes.