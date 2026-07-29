"""
Utility functions for the
AI-Augmented Interbank Compliance Demo.
"""

from pathlib import Path
from datetime import datetime


class Console:

    @staticmethod
    def line(length: int = 60):
        print("=" * length)

    @staticmethod
    def title(text: str):
        Console.line()
        print(text.center(60))
        Console.line()

    @staticmethod
    def section(text: str):
        print(f"\n{text}")
        print("-" * len(text))


class ReportGenerator:

    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent

        self.report_path = (
            project_root /
            "output" /
            "report.txt"
        )

    def generate(
        self,
        customer: dict,
        entity: dict,
        prediction: dict,
        explanation: dict,
        blockchain_record: dict,
    ):

        report = []

        report.append("=" * 60)
        report.append("AI-AUGMENTED INTERBANK COMPLIANCE REPORT")
        report.append("=" * 60)

        report.append("")
        report.append(f"Generated : {datetime.now()}")
        report.append("")

        report.append("CUSTOMER INFORMATION")
        report.append("--------------------")
        report.append(f"Name      : {customer['name']}")
        report.append(f"DOB       : {customer['dob']}")
        report.append(f"Country   : {customer['country']}")
        report.append(f"Amount    : ${customer['amount']:,}")

        report.append("")
        report.append("ENTITY RESOLUTION")
        report.append("-----------------")
        report.append(f"Matched           : {entity['matched']}")
        report.append(f"Matched Name      : {entity['matched_name']}")
        report.append(f"Similarity        : {entity['similarity']}%")
        report.append(f"Risk Level        : {entity['risk_level']}")
        report.append(f"Sanction List     : {entity['sanction_list']}")

        report.append("")
        report.append("AI PREDICTION")
        report.append("-------------")
        report.append(
            f"Prediction : {prediction['prediction']}"
        )
        report.append(
            f"Confidence : {prediction['confidence']:.2%}"
        )

        report.append("")
        report.append("TOP AI FACTORS")
        report.append("--------------")

        for factor in explanation["top_factors"][:5]:

            report.append(
                f"{factor['feature']:20}"
                f"{factor['impact']:+.4f}"
            )

        report.append("")
        report.append("BLOCKCHAIN")
        report.append("----------")
        report.append(
            f"Transaction ID : "
            f"{blockchain_record['transaction_id']}"
        )
        report.append(
            f"Hash           : "
            f"{blockchain_record['hash']}"
        )

        report.append("")
        report.append("=" * 60)

        self.report_path.write_text(
            "\n".join(report),
            encoding="utf-8",
        )

        return self.report_path


def print_prediction(prediction: dict):

    Console.section("Prediction")

    print(f"Result      : {prediction['prediction']}")
    print(f"Confidence  : {prediction['confidence']:.2%}")


def print_entity(entity: dict):

    Console.section("Entity Resolution")

    print(f"Matched        : {entity['matched']}")
    print(f"Watchlist Name : {entity['matched_name']}")
    print(f"Similarity     : {entity['similarity']}%")
    print(f"Risk Level     : {entity['risk_level']}")


def print_explanation(explanation: dict):

    Console.section("Top AI Factors")

    for factor in explanation["top_factors"][:5]:

        print(
            f"{factor['feature']:20}"
            f"{factor['impact']:+.4f}"
        )