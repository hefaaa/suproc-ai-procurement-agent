class ProfessionalTool:

    def __init__(self,kb):

        self.df = kb.professionals

    def recommend(self,skill):

        return self.df[
            self.df["Skill"].str.contains(
                skill,
                case=False,
                na=False
            )
        ]