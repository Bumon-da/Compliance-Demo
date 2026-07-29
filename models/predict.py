"""
Prediction module for the
AI-Augmented Interbank Compliance Demo.
"""

from pathlib import Path
import joblib
import pandas as pd


class CompliancePredictor:
    """Loads the trained model and performs predictions."""

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent

        self.model_path = project_root / "models" / "model.pkl"

        if not self.model_path.exists():
            raise FileNotFoundError(
                "Model not found.\n"
                "Please run:\n"
                "python models/train.py"
            )

        self.model = joblib.load(self.model_path)

    def predict(self, features: dict) -> dict:
        """
        Predict compliance risk.

        Parameters
        ----------
        features : dict
            Dictionary containing the feature values.

        Returns
        -------
        dict
            Prediction results.
        """

        df = pd.DataFrame([features])

        prediction = self.model.predict(df)[0]

        probabilities = self.model.predict_proba(df)[0]

        confidence = probabilities[prediction]

        return {
            "prediction": (
                "REAL RISK"
                if prediction == 1
                else "FALSE POSITIVE"
            ),
            "prediction_id": int(prediction),
            "confidence": round(float(confidence), 4),
            "probabilities": {
                "false_positive": round(float(probabilities[0]), 4),
                "real_risk": round(float(probabilities[1]), 4),
            },
        }


if __name__ == "__main__":

    predictor = CompliancePredictor()

    sample_features = {
        "name_similarity": 0.95,
        "dob_match": 1,
        "country_risk": 0,
        "amount": 25000,
        "previous_history": 0,
        "watchlist_match": 1,
    }

    result = predictor.predict(sample_features)

    print("=" * 40)
    print("Prediction Result")
    print("=" * 40)

    print(f"Prediction : {result['prediction']}")
    print(f"Confidence : {result['confidence']:.2%}")

    print("\nProbability Distribution")

    print(
        f"False Positive : "
        f"{result['probabilities']['false_positive']:.2%}"
    )

    print(
        f"Real Risk      : "
        f"{result['probabilities']['real_risk']:.2%}"
    )