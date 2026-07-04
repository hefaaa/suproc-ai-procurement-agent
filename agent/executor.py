from tools.knowledge_base import KnowledgeBase
from tools.supplier_tool import SupplierTool
from tools.professional_tool import ProfessionalTool
from tools.project_tool import ProjectTool
from tools.procurement_tool import ProcurementTool
from tools.opportunity_tool import OpportunityTool

from tools.filter import FilterTool
from tools.ranking import RankingTool
from tools.validation import ValidationTool
from tools.correction import CorrectionTool


class AgentExecutor:

    def __init__(self):

        self.kb = KnowledgeBase()

        self.suppliers = SupplierTool(self.kb)
        self.professionals = ProfessionalTool(self.kb)
        self.projects = ProjectTool(self.kb)
        self.procurement = ProcurementTool(self.kb)
        self.opportunities = OpportunityTool(self.kb)

        self.filter = FilterTool()
        self.ranker = RankingTool()
        self.validator = ValidationTool()
        self.corrector = CorrectionTool()

    def execute(self, requirement):

        print("\n" + "=" * 60)
        print("STEP 1 : SEARCHING")
        print("=" * 60)

        supplier_results = self.suppliers.search(requirement.category)

        print(f"Found {len(supplier_results)} suppliers")

        print("\n" + "=" * 60)
        print("STEP 2 : APPLYING HARD CONSTRAINTS")
        print("=" * 60)

        filtered = self.filter.filter_by_constraints(
            suppliers=supplier_results,
            min_capacity=requirement.min_capacity,
            max_delivery_days=requirement.max_delivery_days,
            certification="Food Grade",
            availability="Available"
        )

        print(f"{len(filtered)} suppliers satisfy hard constraints")

        print("\n" + "=" * 60)
        print("STEP 3 : RANKING")
        print("=" * 60)

        ranked = self.ranker.rank_suppliers(filtered)

        print(f"Ranked {len(ranked)} suppliers")

        print("\n" + "=" * 60)
        print("STEP 4 : VALIDATION")
        print("=" * 60)

        valid_suppliers, report = self.validator.validate(
            ranked,
            requirement
        )

        passed = len([r for r in report if r["Status"] == "PASS"])
        failed = len([r for r in report if r["Status"] == "FAIL"])

        print(f"Passed : {passed}")
        print(f"Failed : {failed}")

        corrected_suppliers, correction_report = self.corrector.correct(
            valid_suppliers,
            report,
            requirement
        )

        corrected_suppliers = corrected_suppliers[
            :requirement.requested_results
        ]

        # --------------------------------------------------
        # Additional Knowledge Sources
        # --------------------------------------------------

        professionals = self.professionals.recommend("Procurement")

        projects = self.projects.related_projects("Packaging")

        history = self.procurement.similar_requests(
            requirement.category
        )

        opportunities = self.opportunities.related(
            "Procurement"
        )

        return {

            "recommendations": corrected_suppliers,

            "validation_report": report,

            "correction_report": correction_report,

            "professionals": professionals,

            "projects": projects,

            "history": history,

            "opportunities": opportunities

        }
    def search_and_rank(self, requirement):

        supplier_results = self.suppliers.search(
            requirement.category
        )

        filtered = self.filter.filter_by_constraints(
            supplier_results,
            requirement.min_capacity,
            requirement.max_delivery_days,
            "Food Grade",
            "Available"
        )

        corrected_suppliers, report, correction_report = self.corrector.correct(
        self,
        requirement
    )