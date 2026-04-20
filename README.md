# ICU Mortality Risk Prediction — Healthcare Machine Learning Project

[![MIMIC-III](https://img.shields.io/badge/Data-MIMIC--III-0a3f6e?style=flat-square&logo=databricks&logoColor=white)](https://www.kaggle.com/datasets/drscarlat/mimic3c)
[![Python](https://img.shields.io/badge/Python-3.8-1a1a2e?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-e07b39?style=flat-square)](https://xgboost.readthedocs.io/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit%20Live-ff4b4b?style=flat-square)](https://icu-mortality-risk-prediction-ldqgvlkdtpd9btbdkxxak3.streamlit.app/)
[![Status](https://img.shields.io/badge/Status-Complete-2ecc71?style=flat-square)](https://github.com/KrishnaKJoshi1/icu-mortality-risk-prediction)

XGBoost pipeline trained on MIMIC-III ICU data — ROC-AUC 0.90, Recall ≥ 0.85 after threshold tuning — deployed as a live Streamlit application for real-time patient risk scoring.

---

## Problem Context

In ICU environments, delayed recognition of deteriorating patients can significantly impact survival outcomes.

This project addresses that challenge by developing a predictive risk modeling framework capable of identifying high-mortality-risk patients early using structured clinical variables.

The system is designed with a patient-safety-first evaluation strategy — prioritizing Recall to minimize missed high-risk patients.

---

## Dataset

This project uses an aggregated ICU clinical dataset derived from MIMIC-III electronic health records.

Due to data usage and repository size considerations, the full dataset is **not included** in this repository.

To reproduce the notebook locally:

1. Download the dataset from Kaggle
2. Place the file as `mimic3c.csv` in the project root directory
3. Update file paths if needed

Dataset Source:
https://www.kaggle.com/datasets/drscarlat/mimic3c

---

## Live Application Demo

Explore the deployed interactive application:

🔗 [Launch Live App](https://icu-mortality-risk-prediction-ldqgvlkdtpd9btbdkxxak3.streamlit.app/)

The Streamlit interface enables:

- Patient record selection
- Real-time mortality prediction
- Probability risk scoring
- Color-coded triage classification (Low / Moderate / Elevated / Critical)

![Streamlit Demo](images/streamlit_demo.png)

---

## Modeling Approach

Multiple supervised learning models were trained and evaluated:

- Logistic Regression (Baseline)
- Random Forest
- XGBoost — Final Selected Model

Key modeling steps:

- Clinical feature preprocessing
- Missing value handling
- Encoding & scaling
- Class imbalance consideration
- Cross-model comparison

Model selection prioritized **Recall** to minimize false negatives — aligning with ICU risk detection priorities.

---

## Model Performance

| Model | Recall | ROC-AUC | Notes |
|---|---|---|---|
| **XGBoost** | **≥ 0.85** | **0.90** | **Selected — best Recall + AUC** |
| Random Forest | lower | strong | Ensemble baseline |
| Logistic Regression | lowest | moderate | Linear baseline |

> Recall was chosen as the primary metric. In ICU mortality prediction, a missed high-risk patient carries far greater clinical cost than a false alarm. Threshold was tuned to target Recall ≥ 0.85.

![ROC Curve](images/roc_curve.png)

![Precision-Recall Curve](images/precision_recall_curve.png)

![Confusion Matrix](images/confusion_matrix.png)

---

## Top Predictive Features — XGBoost

| Rank | Feature | Clinical meaning |
|---|---|---|
| 1 | `TotalNumInteract` | Total clinical interactions — strongest severity signal |
| 2 | `NumLabs` | Lab order volume — active investigation intensity |
| 3 | `NumCallouts` | Care escalation callouts |
| 4 | `NumMicroLabs` | Microbiology orders — infection and sepsis indicator |
| 5 | `NumCPTevents` | Procedure count — illness complexity proxy |
| 6 | `age` | Older patients carry higher baseline mortality risk |
| 7 | `NumInput` | Fluid and medication inputs — critical care intensity |
| 8 | `admit_type_EMERGENCY` | Emergency admission — higher acuity on arrival |

![Feature Importance](images/feature_importance.png)

---

## Deployment Pipeline

A production-ready pipeline was constructed integrating:

- Data preprocessing
- Feature encoding
- Scaling transformations
- XGBoost inference

The serialized pipeline artifact (`artifacts/pipeline.pkl`) ensures consistent transformation logic and reproducible predictions during deployment.

---

## Clinical Relevance

Early mortality risk identification supports:

- ICU triage prioritization
- Monitoring escalation decisions
- Resource allocation planning
- Critical care intervention timing

The recall-optimized modeling strategy aligns with patient-safety-focused healthcare AI deployment principles.

---

## Limitations

- Dataset sourced from a single institution (Beth Israel Deaconess, Boston) — results may not generalise to other hospital systems
- Model is intended to support clinical decision-making, not replace it
- SHAP-based interpretability was explored but excluded due to environment compatibility — planned for a future version
- Bias analysis across age, gender, and insurance groups is available in `notebooks/05_bias_analysis.ipynb`

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

---

## Technology Stack

| Layer | Technology |
|---|---|
| Data | MIMIC-III (Kaggle / PhysioNet) |
| Language | Python 3.8 |
| ML | scikit-learn, XGBoost, pandas, NumPy, joblib |
| Visualisation | matplotlib, seaborn |
| Deployment | Streamlit |

---

## Future Enhancements

Potential extensions include:

- Time-series ICU modeling with hourly vitals
- SHAP-based explainability integration
- Survival analysis (time-to-event modeling)
- Real-time EHR connectivity
- External validation on MIMIC-IV or eICU-CRD

---

## Citation

```
@misc{icu_mortality_joshi_2025,
  title  = {ICU Mortality Risk Prediction Using Structured EHR Data},
  author = {Joshi, Krishna K.},
  year   = {2025},
  note   = {Healthcare ML Portfolio Project — MIMIC-III},
  url    = {https://github.com/KrishnaKJoshi1/icu-mortality-risk-prediction}
}
```

---

Healthcare Machine Learning Portfolio Project
Focused on predictive analytics, clinical AI modeling, and deployment-ready healthcare ML systems.
