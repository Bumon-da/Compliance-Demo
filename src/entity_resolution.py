"""
Entity Resolution Module

Compares a customer's information against the AML watchlist
using fuzzy string matching.
"""

from pathlib import Path
import pandas as pd
from rapidfuzz import fuzz


class EntityResolver:
    """Finds the best matching person from the AML watchlist."""

    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent

        self.watchlist_path = project_root / "data" / "watchlist.csv"

        self.watchlist = pd.read_csv(self.watchlist_path)

    def find_best_match(
        self,
        customer_name: str,
        customer_dob: str,
    ) -> dict:
        """
        Returns the highest scoring watchlist match.
        """

        best_match = None
        highest_score = 0

        for _, person in self.watchlist.iterrows():

            score = fuzz.ratio(
                customer_name.lower(),
                person["name"].lower(),
            )

            # Give bonus if DOB matches
            if customer_dob == person["dob"]:
                score += 5

            if score > highest_score:
                highest_score = score
                best_match = person

        if best_match is None:
            return {
                "matched": False,
                "similarity": 0,
            }

        return {
            "matched": highest_score >= 85,
            "watchlist_id": best_match["id"],
            "matched_name": best_match["name"],
            "dob": best_match["dob"],
            "country": best_match["country"],
            "risk_level": best_match["risk_level"],
            "sanction_list": best_match["sanction_list"],
            "similarity": round(min(highest_score, 100), 2),
        }


if __name__ == "__main__":

    resolver = EntityResolver()

    result = resolver.find_best_match(
        customer_name="Jon Smith",
        customer_dob="1992-06-15",
    )

    print("=" * 40)
    print("Entity Resolution Result")
    print("=" * 40)

    for key, value in result.items():
        print(f"{key:15}: {value}")