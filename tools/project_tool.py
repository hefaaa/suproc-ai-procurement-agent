class ProjectTool:

    def __init__(self,kb):

        self.df = kb.projects

    def related_projects(self,category):

        return self.df[
            self.df["Category"].str.contains(
                category,
                case=False,
                na=False
            )
        ]