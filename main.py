"""
AI-Augmented Interbank Compliance Demo

Run:
    python main.py
"""

from src.entity_resolution import EntityResolver
from src.feature_builder import FeatureBuilder
from src.explain import ComplianceExplainer
from src.blockchain import BlockchainLogger
from src.utils import (
    Console,
    ReportGenerator,
    print_entity,
    print_prediction,
    print_explanation,
)

from models.predict import CompliancePredictor


def main():

    Console.title(
        "AI-Augmented Interbank Compliance Network"
    )

    # --------------------------------------------------
    # Example Customer
    # --------------------------------------------------

    customer = {
        "name": "Jon Smith",
        "dob": "1992-06-15",
        "country": "Germany",
        "amount": 25000,
        "previous_history": False,
    }

    Console.section("Customer")

    for key, value in customer.items():
        print(f"{key:18}: {value}")

    # --------------------------------------------------
    # Entity Resolution
    # --------------------------------------------------

    resolver = EntityResolver()

    entity = resolver.find_best_match(
        customer_name=customer["name"],
        customer_dob=customer["dob"],
    )

    print_entity(entity)

    # --------------------------------------------------
    # Feature Engineering
    # --------------------------------------------------

    features = FeatureBuilder.build(
        customer,
        entity,
    )

    Console.section("ML Features")

    for key, value in features.items():
        print(f"{key:20}: {value}")

    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    predictor = CompliancePredictor()

    prediction = predictor.predict(features)

    print_prediction(prediction)

    # --------------------------------------------------
    # SHAP Explanation
    # --------------------------------------------------

    explainer = ComplianceExplainer()

    explanation = explainer.explain(features)

    print_explanation(explanation)

    # --------------------------------------------------
    # Blockchain
    # --------------------------------------------------

    blockchain = BlockchainLogger()

    transaction = blockchain.add_record(
        customer,
        prediction,
        explanation,
    )

    Console.section("Blockchain")

    print(
        f"Transaction ID : "
        f"{transaction['transaction_id']}"
    )

    print(
        f"Hash           : "
        f"{transaction['hash']}"
    )

    # --------------------------------------------------
    # Generate Report
    # --------------------------------------------------

    report = ReportGenerator()

    report_path = report.generate(
        customer,
        entity,
        prediction,
        explanation,
        transaction,
    )

    Console.section("Report")

    print(report_path)

    Console.line()

    print("Demo Completed Successfully!")

    Console.line()


if __name__ == "__main__":
    main()