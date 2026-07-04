class Validator:

    def validate(self, suppliers, requirement):

        report = []
        valid = []
        seen = set()

        dangerous = [
            "ignore previous instructions",
            "approve immediately",
            "send email",
            "delete database",
            "system prompt",
            "ignore validation"
        ]

        for supplier in suppliers:

            reasons = []

            # -----------------------------
            # Exists
            # -----------------------------

            if not supplier.get("SupplierID"):
                reasons.append("Supplier ID missing")

            # -----------------------------
            # Duplicate
            # -----------------------------

            if supplier["SupplierID"] in seen:
                reasons.append("Duplicate recommendation")

            seen.add(supplier["SupplierID"])

            # -----------------------------
            # Prompt Injection
            # -----------------------------

            description = str(
                supplier.get("Description", "")
            ).lower()

            for phrase in dangerous:

                if phrase in description:

                    reasons.append(
                        f"Prompt injection detected ({phrase})"
                    )

                    break

            # -----------------------------
            # Entity Type
            # -----------------------------

            if requirement.entity_type.lower() not in [
                "supplier",
                "suppliers"
            ]:
                reasons.append("Incorrect entity type")

            # -----------------------------
            # Certification
            # -----------------------------

            if supplier["Certification"] != "Food Grade":
                reasons.append("Food Grade certification missing")

            # -----------------------------
            # Capacity
            # -----------------------------

            if supplier["Capacity"] < requirement.min_capacity:
                reasons.append(
                    f"Capacity below required ({supplier['Capacity']})"
                )

            # -----------------------------
            # Delivery
            # -----------------------------

            if supplier["DeliveryDays"] > requirement.max_delivery_days:
                reasons.append(
                    f"Delivery exceeds {requirement.max_delivery_days} days"
                )

            # -----------------------------
            # Availability
            # -----------------------------

            if supplier["Availability"] != "Available":
                reasons.append("Supplier unavailable")

            # -----------------------------
            # Match Score
            # -----------------------------

            if supplier["MatchScore"] > 100:
                reasons.append("Invalid match score")

            # -----------------------------
            # PASS / FAIL
            # -----------------------------

            if len(reasons) == 0:

                valid.append(supplier)

                report.append({
                    "SupplierID": supplier["SupplierID"],
                    "Status": "PASS"
                })

            else:

                report.append({
                    "SupplierID": supplier["SupplierID"],
                    "Status": "FAIL",
                    "Reasons": reasons
                })

        # -----------------------------
        # Requested Count
        # -----------------------------

        if len(valid) < requirement.requested_results:

            report.append({

                "SupplierID": "-",

                "Status": "WARNING",

                "Reasons": [

                    f"Only {len(valid)} valid suppliers found."

                ]

            })

        return valid, report