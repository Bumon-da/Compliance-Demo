"""
Train the Random Forest model for the
AI-Augmented Interbank Compliance Demo.
"""

from pathlib import Path
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split


# -----------------------------
# Paths
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "transactions.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "model.pkl"


# -----------------------------
# Load Dataset
# -----------------------------

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print(f"Dataset loaded successfully ({len(df)} samples).")


# -----------------------------
# Prepare Data
# -----------------------------

X = df.drop(columns=["label"])
y = df["label"]


# -----------------------------
# Split Dataset
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)


# -----------------------------
# Train Model
# -----------------------------

print("\nTraining Random Forest model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

model.fit(X_train, y_train)

print("Training complete.")


# -----------------------------
# Evaluation
# -----------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Evaluation")
print("-" * 40)

print(f"Accuracy : {accuracy:.2%}")

print("\nClassification Report")

print(classification_report(y_test, predictions))

print("Confusion Matrix")

print(confusion_matrix(y_test, predictions))


# -----------------------------
# Save Model
# -----------------------------

joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to:\n{MODEL_PATH}")