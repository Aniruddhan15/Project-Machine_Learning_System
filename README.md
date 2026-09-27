# Project-Machine_Learning_System
End to End ML System in collaboration with Teammate Hamshika 


# 🌌 Geomagnetic Storm Early-Warning System

> **From solar wind → ML prediction → early warning.**

An end-to-end **MLOps system** that uses historical space-weather data to predict whether a **geomagnetic storm (Kp ≥ 5) will occur 3 hours ahead**, then serves live predictions using real-time solar-wind observations.

The project focuses on building the **complete ML lifecycle** — reproducible data pipelines, experiment tracking, deployment, CI/CD, and production monitoring.

---

## ☀️ Why This Project?

Geomagnetic storms can disrupt:

⚡ Power grids  
🛰️ Satellites  
📡 GPS systems  
✈️ Polar aviation communications  

A few hours of advance warning can give operators time to take preventive action.

**Goal:**

```text
Live Solar Wind Data
        ↓
   ML Pipeline
        ↓
 Storm Probability
        ↓
  ⚠️ 3-Hour Warning
```

---

## 🧠 ML Problem

**Task:** Binary Classification

```text
Will Kp ≥ 5 three hours from now?

1 → 🌩️ Storm Expected
0 → ☀️ No Storm Expected
```

### Data

**Training:** NASA OMNI2 hourly space-weather observations  
**Live inference:** NOAA DSCOVR solar-wind feed

The historical dataset spans **2000–2025 (~228K hourly observations)**.

Because geomagnetic storms are relatively rare, evaluation emphasizes **storm recall, precision, F1-score, and PR-AUC** rather than accuracy alone.

---

## 🏗️ System Architecture

```text
          NASA OMNI2
              │
              ▼
     Data Validation & DVC
              │
              ▼
      Feature Engineering
              │
              ▼
       Model Training
              │
              ▼
      MLflow Registry
              │
              ▼
NOAA Live Data → FastAPI → Prediction
                           │
                           ▼
                     📊 Dashboard
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
             Monitoring        Drift Detection
```

---

## ⚙️ Tech Stack

**ML & Data**  
`Python` · `Pandas` · `Scikit-learn` · `XGBoost/LightGBM` · `Pandera`

**MLOps**  
`MLflow` · `DVC` · `pytest` · `GitHub Actions`

**Serving & Deployment**  
`FastAPI` · `Pydantic` · `Docker` · `AWS`

**Infrastructure & Orchestration**  
`Airflow/Prefect` · `Terraform` · `Kubernetes`

**Monitoring**  
`Prometheus` · `Grafana` · `Evidently AI`

---

## 🔄 Production Workflow

```text
Ingest → Validate → Transform → Train → Evaluate
                                      ↓
                                  Register
                                      ↓
Live NOAA Data → Validate → Predict → Monitor
```

The production system is designed around three principles:

**Reproducibility** 🔁 — versioned data, code, experiments, and models  
**Reliability** 🛡️ — validation and explicit handling of missing/stale data  
**Observability** 📊 — monitoring both system health and model behavior

---

## 🎯 Project Goal

This project is intentionally more than a model-training notebook.

The objective is to demonstrate how an ML model becomes a **reproducible, deployable, monitored production system** capable of continuously generating predictions from live data.

---

## 👨‍💻 Author

**Aniruddhan Narasimhan**

M.S. Applied Machine Learning @ University of Maryland, College Park