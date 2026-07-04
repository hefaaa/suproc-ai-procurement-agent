class ProcurementTool:

    def __init__(self,kb):

        self.df=kb.procurement

    def similar_requests(self,category):

        return self.df[
            self.df["Category"].str.contains(
                category,
                case=False,
                na=False
            )
        ]