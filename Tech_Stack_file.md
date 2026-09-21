This is the project stack for the end to end ML System Portfolio Project


# MLOps Project: Tech Stack

I'm building an end-to-end MLOps project. The goal isn't just to train a
model, but to take it all the way from raw data to a deployed, monitored
service. I picked a stack that works for either a classification or a
forecasting problem, so I can settle on the dataset without redoing the
setup.

## Data
- Git + GitHub for code, branches, and pull requests.
- DVC (with an S3 remote) to version datasets and pipeline stages, so any
  result can be reproduced.
- S3 + Parquet to store raw and processed data.
- Postgres as the MLflow backend, and later to log predictions so I can
  compare them with real outcomes.
- pandas for cleaning and feature engineering (Polars if the data gets heavy).
- Pandera for schema and quality checks, so bad data fails loudly instead
  of silently breaking the model.

## Modeling
- scikit-learn for simple baselines, then LightGBM or XGBoost as the main
  model. The baseline comes first so the fancier model has to earn its place.
- Optuna for hyperparameter tuning, if time allows.
- MLflow to track experiments and to version models in its registry.

## Pipeline and serving
- Airflow (or Prefect) to schedule ingest, validate, train, and evaluate.
- FastAPI + Pydantic for a prediction API with validated inputs.
- pytest, ruff, and pre-commit to keep the code tested and clean.

## Deployment
- Docker and docker-compose to package the app and run everything locally.
- GitHub Actions to test, build the image, push to ECR, and deploy.
- AWS: ECR and S3, with ECS Fargate or EC2 to run the service.
- Terraform to create the cloud resources as code.
- Kubernetes (kind locally) with Helm. I'll only run EKS briefly for a demo
  because of the cost.

## Monitoring
- Prometheus for latency, request counts, and errors.
- Evidently AI for data drift and model performance.
- Grafana to put both system and model health on one dashboard.

## Nice to have
- Streamlit for a simple demo UI.
- ArgoCD for automated deploys, only if I have time left.

## How I'm approaching it
I'm building this in three stages so there's always a working version:
1. Core: data, model, tracking, API, Docker, CI, and a cloud deployment.
2. Production: scheduled retraining, monitoring, and drift checks.
3. Stretch: Kubernetes, Terraform, and extras.

Some of these tools are new to me, so I'm learning each one as I reach it
and will update this file as I find out what works.