"""
Explainability Module

Uses SHAP to explain why the ML model
made its prediction.
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import shap


class ComplianceExplainer:
    """Generate SHAP explanations for compliance predictions."""

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent
        model_path = project_root / "models" / "model.pkl"

        if not model_path.exists():
            raise FileNotFoundError(
                f"Model not found at:\n{model_path}\n\n"
                "Train the model first with:\n"
                "python models/train.py"
            )

        self.model = joblib.load(model_path)
        self.explainer = shap.TreeExplainer(self.model)

    def explain(self, features: dict) -> dict:
        """
        Generate a SHAP explanation for one transaction.

        Parameters
        ----------
        features : dict
            Features used by the Random Forest model.

        Returns
        -------
        dict
            Predicted class and SHAP contribution of each feature.
        """

        # Keep feature order consistent with the trained model
        if hasattr(self.model, "feature_names_in_"):
            feature_names = list(self.model.feature_names_in_)
        else:
            feature_names = list(features.keys())

        df = pd.DataFrame(
            [[features[name] for name in feature_names]],
            columns=feature_names,
        )

        prediction = int(self.model.predict(df)[0])

        # Modern SHAP API
        explanation = self.explainer(df)
        values = np.asarray(explanation.values)

        """
        Depending on SHAP version, RandomForestClassifier can return:

        (samples, features)
        or
        (samples, features, classes)

        For binary classification we want the SHAP values
        corresponding to the class predicted by the model.
        """

        if values.ndim == 3:
            # Shape:
            # (samples, features, classes)

            feature_impacts = values[0, :, prediction]

        elif values.ndim == 2:
            # Shape:
            # (samples, features)

            feature_impacts = values[0]

        elif values.ndim == 1:
            feature_impacts = values

        else:
            raise ValueError(
                f"Unexpected SHAP output shape: {values.shape}"
            )

        contributions = []

        for feature_name, impact in zip(
            feature_names,
            feature_impacts,
        ):
            contributions.append(
                {
                    "feature": feature_name,
                    "impact": round(float(impact), 4),
                }
            )

        # Most influential features first
        contributions.sort(
            key=lambda item: abs(item["impact"]),
            reverse=True,
        )

        return {
            "prediction": prediction,
            "top_factors": contributions,
        }


if __name__ == "__main__":
    explainer = ComplianceExplainer()

    sample = {
        "name_similarity": 0.95,
        "dob_match": 1,
        "country_risk": 0,
        "amount": 25000,
        "previous_history": 0,
        "watchlist_match": 1,
    }

    result = explainer.explain(sample)

    print("=" * 50)
    print("SHAP Explanation")
    print("=" * 50)

    print(
        "Prediction:",
        "REAL RISK"
        if result["prediction"] == 1
        else "FALSE POSITIVE",
    )

    print("\nFeature Contributions")

    for factor in result["top_factors"]:
        print(
            f"{factor['feature']:20}"
            f"{factor['impact']:+.4f}"
        )