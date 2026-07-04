class SupplierTool:

    def __init__(self, kb):
        self.df = kb.suppliers

    def search(self, category):

        if category == "":
            return self.df.to_dict("records")

        results = self.df[
            self.df["Category"].str.contains(
                category,
                case=False,
                na=False
            )
        ]

        return results.to_dict("records")