import pandas as pd


class KnowledgeBase:

    def __init__(self):

        self.suppliers = pd.read_csv("data/suppliers.csv")

        self.professionals = pd.read_csv("data/professionals.csv")

        self.projects = pd.read_csv("data/projects.csv")

        self.opportunities = pd.read_csv("data/opportunities.csv")

        self.procurement = pd.read_csv(
            "data/procurement_requests.csv"
        )