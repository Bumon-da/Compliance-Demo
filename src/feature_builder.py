"""
Feature Builder

Converts customer information and entity resolution results
into the feature vector expected by the ML model.
"""

from typing import Dict


class FeatureBuilder:
    """Builds ML-ready features."""

    # Countries considered high-risk for this demo
    HIGH_RISK_COUNTRIES = {
        "North Korea",
        "Iran",
        "Syria",
        "Russia",
        "Iraq",
    }

    @staticmethod
    def build(
        customer: Dict,
        entity_result: Dict,
    ) -> Dict:
        """
        Build feature dictionary for ML prediction.

        Parameters
        ----------
        customer : dict
            Customer information.

        entity_result : dict
            Result returned from EntityResolver.

        Returns
        -------
        dict
            Features ready for Random Forest.
        """

        similarity = entity_result.get("similarity", 0) / 100

        dob_match = int(
            customer["dob"] == entity_result.get("dob")
        )

        watchlist_match = int(
            entity_result.get("matched", False)
        )

        previous_history = int(
            customer.get("previous_history", False)
        )

        amount = customer["amount"]

        country_risk = int(
            customer["country"] in FeatureBuilder.HIGH_RISK_COUNTRIES
        )

        return {
            "name_similarity": round(similarity, 3),
            "dob_match": dob_match,
            "country_risk": country_risk,
            "amount": amount,
            "previous_history": previous_history,
            "watchlist_match": watchlist_match,
        }


if __name__ == "__main__":

    customer = {
        "name": "Jon Smith",
        "dob": "1992-06-15",
        "country": "Germany",
        "amount": 25000,
        "previous_history": False,
    }

    entity_result = {
        "matched": True,
        "similarity": 96,
        "dob": "1992-06-15",
    }

    features = FeatureBuilder.build(
        customer,
        entity_result,
    )

    print("=" * 40)
    print("Generated Features")
    print("=" * 40)

    for key, value in features.items():
        print(f"{key:20}: {value}")