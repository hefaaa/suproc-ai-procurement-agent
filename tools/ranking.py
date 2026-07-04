class RankingTool:

    def rank_suppliers(self, suppliers):

        ranked = []

        for supplier in suppliers:

            breakdown = {}

            score = 0

            # ------------------------------------------------
            # Product Relevance (30)
            # ------------------------------------------------
            relevance = 30
            breakdown["Product Relevance"] = relevance
            score += relevance

            # ------------------------------------------------
            # Location Suitability (20)
            # ------------------------------------------------
            if supplier["Location"] in [
                "Bengaluru",
                "Chennai",
                "Hyderabad",
                "Kochi",
                "Coimbatore",
                "Mysuru",
                "Madurai",
                "Trivandrum",
                "Visakhapatnam",
                "Vijayawada"
            ]:
                location = 20
            else:
                location = 10

            breakdown["Location"] = location
            score += location

            # ------------------------------------------------
            # Hard Constraints (25)
            # ------------------------------------------------
            constraints = 25

            if supplier["Certification"] != "Food Grade":
                constraints -= 10

            if supplier["Availability"] != "Available":
                constraints -= 15

            constraints = max(0, constraints)

            breakdown["Hard Constraints"] = constraints
            score += constraints

            # ------------------------------------------------
            # Capacity & Availability (15)
            # ------------------------------------------------
            capacity = 15

            if supplier["Capacity"] < 10000:
                capacity = 5

            breakdown["Capacity"] = capacity
            score += capacity

            # ------------------------------------------------
            # Reputation (10)
            # ------------------------------------------------
            rating = supplier["Rating"]

            if rating >= 4.8:
                reputation = 10
            elif rating >= 4.5:
                reputation = 8
            elif rating >= 4:
                reputation = 6
            else:
                reputation = 3

            breakdown["Reputation"] = reputation
            score += reputation

            supplier["MatchScore"] = score
            supplier["Breakdown"] = breakdown

            ranked.append(supplier)

        ranked.sort(
            key=lambda x: x["MatchScore"],
            reverse=True
        )

        return ranked