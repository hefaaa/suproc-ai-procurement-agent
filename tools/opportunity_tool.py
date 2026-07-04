class OpportunityTool:

    def __init__(self,kb):

        self.df=kb.opportunities

    def related(self,skill):

        return self.df[
            self.df["RequiredSkill"].str.contains(
                skill,
                case=False,
                na=False
            )
        ]