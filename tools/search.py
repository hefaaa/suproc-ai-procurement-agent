import pandas as pd


class SearchTool:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def search_entities(self, category=None, location=None):
        """
        Search suppliers by category and/or location.
        """
        results = self.df.copy()

        if category:
            results = results[
                results["Category"].str.contains(category, case=False, na=False)
            ]

        if location:
            results = results[
                results["Location"].str.contains(location, case=False, na=False)
            ]

        return results

    def get_entity_details(self, supplier_id):
        """
        Return a supplier by ID.
        """
        result = self.df[self.df["SupplierID"] == supplier_id]

        if result.empty:
            return None

        return result.iloc[0]