class Planner:

    def create_plan(self, requirement):

        return [
            "Search suppliers by category",
            "Apply hard constraints",
            "Rank matching suppliers",
            "Validate recommendations",
            "Prepare outreach draft",
            "Await human approval"
        ]

    def display_plan(self, plan):

        print("\n" + "=" * 60)
        print("EXECUTION PLAN")
        print("=" * 60)

        for i, step in enumerate(plan, start=1):
            print(f"{i}. {step}")

        print("=" * 60)