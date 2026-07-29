# AI-Augmented Interbank Compliance Network (Prototype)

## Overview

The AI-Augmented Interbank Compliance Network is a proof-of-concept that demonstrates how Artificial Intelligence and blockchain-inspired audit mechanisms can be integrated to improve interbank AML (Anti-Money Laundering) and KYC (Know Your Customer) compliance workflows.

Traditional compliance systems generate a high volume of false-positive alerts, resulting in significant manual investigation efforts. This prototype introduces an AI-assisted decision layer capable of performing entity resolution, risk classification, and explainable predictions while maintaining an immutable audit log through a simulated blockchain.

This repository serves as a technical demonstration of the proposed architecture and is intended for educational and research purposes.

---

## Objectives

* Reduce false-positive AML/KYC compliance alerts through intelligent risk assessment.
* Perform entity resolution using fuzzy matching techniques.
* Classify compliance risk using a supervised machine learning model.
* Provide explainable AI predictions using SHAP.
* Maintain a transparent and tamper-evident audit trail through blockchain-style logging.

---

## Key Features

* Fuzzy entity resolution for customer and watchlist matching
* Machine learning-based compliance risk classification
* Explainable AI using SHAP
* Simulated blockchain audit logging
* Modular and extensible project architecture
* End-to-end compliance workflow demonstration

---

## Project Architecture

```text
Customer Information
        │
        ▼
Entity Resolution
        │
        ▼
Feature Engineering
        │
        ▼
Risk Classification Model
        │
        ▼
SHAP Explainability
        │
        ▼
Blockchain Audit Log
        │
        ▼
Compliance Decision Report
```

---

## Project Structure

```text
compliance-demo/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── transactions.csv
│   └── watchlist.csv
│
├── models/
│   ├── train.py
│   ├── predict.py
│   └── model.pkl
│
├── src/
│   ├── entity_resolution.py
│   ├── feature_builder.py
│   ├── explain.py
│   ├── blockchain.py
│   └── utils.py
│
├── logs/
│   └── blockchain.json
│
└── output/
    └── report.txt
```

---

## Technology Stack

| Category             | Technology                   |
| -------------------- | ---------------------------- |
| Programming Language | Python 3.12+                 |
| Data Processing      | Pandas, NumPy                |
| Machine Learning     | Scikit-learn (Random Forest) |
| Entity Resolution    | RapidFuzz                    |
| Explainable AI       | SHAP                         |
| Model Serialization  | Joblib                       |

---

## Workflow

1. Customer information is received for compliance verification.
2. Entity resolution compares customer details against watchlists using fuzzy matching.
3. Relevant features are generated for machine learning inference.
4. A trained Random Forest model predicts the compliance risk level.
5. SHAP generates feature-level explanations for the prediction.
6. The prediction and supporting metadata are recorded in a simulated blockchain audit log.
7. A compliance report is generated for review.

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd compliance-demo
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Usage

### Train the Model

```bash
python models/train.py
```

### Run the Compliance Pipeline

```bash
python main.py
```

---

## Sample Output

```text
=========================================

Customer: Jon Smith

Prediction: False Positive

Confidence: 97%

Explanation
- Minor spelling variation detected
- Clean transaction history
- Low-risk jurisdiction

Audit Status
Stored successfully in blockchain log

=========================================
```

---

## Current Limitations

This repository is a proof-of-concept and includes several simplifications.

* Uses a simulated blockchain rather than a production permissioned network.
* Uses synthetic demonstration datasets instead of real banking data.
* Implements a simplified compliance workflow.
* Supports a single-machine execution environment.

---

## Future Enhancements

* Hyperledger Fabric integration
* FastAPI backend services
* React-based compliance dashboard
* REST API for interbank communication
* Docker and container orchestration
* Role-based authentication and authorization
* Advanced entity resolution models
* XGBoost and LightGBM model comparison
* Real-time compliance monitoring
* Performance benchmarking and scalability testing

---

## Research Context

This prototype explores the integration of Artificial Intelligence and permissioned blockchain concepts for interbank compliance automation. It demonstrates how explainable machine learning can assist compliance officers by reducing false positives while maintaining transparency, traceability, and auditability.

The project is intended as a foundation for future research into enterprise-grade AI-assisted compliance systems.

---

## License

This project is intended for educational and research purposes.#

## UPDATING THE README FILE 

                          AI-Augmented Interbank Compliance Network

                   ┌──────────────────────────────────────────────┐
                   │               Bank A System                  │
                   └──────────────────────────────────────────────┘
                                      │
                                      │ Transaction Request
                                      ▼
                       ┌──────────────────────────────────┐
                       │      Compliance API Gateway      │
                       │           (FastAPI)              │
                       └──────────────────────────────────┘
                                      │
                 ┌────────────────────┼────────────────────┐
                 │                    │                    │
                 ▼                    ▼                    ▼
      Entity Resolution      ML Risk Prediction      Blockchain Service
      + Feature Creation      + SHAP Explainability      + Smart Contract
                 │                    │                    │
                 └────────────────────┼────────────────────┘
                                      ▼
                          Compliance Decision Engine
                                      │
                                      ▼
                       Store Explanation + Decision Hash
                                      │
                                      ▼
                          Hyperledger Fabric / Quorum
                                      │
                                      ▼
                           Other Banks Read Signal
                                      │
                                      ▼
                           Dashboard & Audit Logs