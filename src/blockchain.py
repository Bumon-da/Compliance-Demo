"""
Blockchain Simulation Module

Stores compliance decisions in a JSON file
with SHA-256 hashes to simulate an immutable ledger.
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime


class BlockchainLogger:
    """Simple blockchain simulation using JSON."""

    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent

        self.log_file = project_root / "logs" / "blockchain.json"

        if not self.log_file.exists():
            self.log_file.write_text("[]", encoding="utf-8")

    def _calculate_hash(self, record: dict) -> str:
        """
        Generate SHA-256 hash of a transaction.
        """

        record_string = json.dumps(
            record,
            sort_keys=True,
        )

        return hashlib.sha256(
            record_string.encode()
        ).hexdigest()

    def add_record(
        self,
        customer: dict,
        prediction: dict,
        explanation: dict,
    ) -> dict:
        """
        Store a compliance decision.
        """

        with open(self.log_file, "r", encoding="utf-8") as file:
            ledger = json.load(file)

        transaction = {
            "transaction_id": f"TX{len(ledger)+1:05}",
            "timestamp": datetime.now().isoformat(timespec="seconds"),

            "customer": {
                "name": customer["name"],
                "dob": customer["dob"],
                "country": customer["country"],
                "amount": customer["amount"],
            },

            "prediction": prediction,

            "top_factors": explanation["top_factors"][:5],
        }

        transaction["hash"] = self._calculate_hash(transaction)

        ledger.append(transaction)

        with open(self.log_file, "w", encoding="utf-8") as file:
            json.dump(
                ledger,
                file,
                indent=4,
            )

        return transaction

    def get_all_transactions(self):
        """
        Return every stored transaction.
        """

        with open(self.log_file, "r", encoding="utf-8") as file:
            return json.load(file)


if __name__ == "__main__":

    logger = BlockchainLogger()

    customer = {
        "name": "Jon Smith",
        "dob": "1992-06-15",
        "country": "Germany",
        "amount": 25000,
    }

    prediction = {
        "prediction": "FALSE POSITIVE",
        "confidence": 0.97,
    }

    explanation = {
        "top_factors": [
            {
                "feature": "name_similarity",
                "impact": -0.38,
            },
            {
                "feature": "watchlist_match",
                "impact": 0.21,
            },
        ]
    }

    record = logger.add_record(
        customer,
        prediction,
        explanation,
    )

    print("=" * 50)
    print("Transaction Stored")
    print("=" * 50)

    print(f"Transaction ID : {record['transaction_id']}")
    print(f"Timestamp      : {record['timestamp']}")
    print(f"Hash           : {record['hash']}")