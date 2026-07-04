class ValidationTool:

    def validate(self, suppliers, requirement):

        report = []

        valid_suppliers = []

        seen = set()

        for supplier in suppliers:

            errors = []

            # Duplicate check
            if supplier["SupplierID"] in seen:
                errors.append("Duplicate supplier")

            seen.add(supplier["SupplierID"])

            # Capacity
            if supplier["Capacity"] < requirement.min_capacity:
                errors.append(
                    f"Capacity {supplier['Capacity']} < {requirement.min_capacity}"
                )

            # Delivery
            if supplier["DeliveryDays"] > requirement.max_delivery_days:
                errors.append(
                    f"Delivery {supplier['DeliveryDays']} > {requirement.max_delivery_days}"
                )

            # Certification
            if supplier["Certification"] != "Food Grade":
                errors.append("Food Grade certification missing")

            # Availability
            if supplier["Availability"] != "Available":
                errors.append("Supplier unavailable")

            if len(errors) == 0:

                report.append({
                    "SupplierID": supplier["SupplierID"],
                    "CompanyName": supplier["CompanyName"],
                    "Status": "PASS"
                })

                valid_suppliers.append(supplier)

            else:

                report.append({
                    "SupplierID": supplier["SupplierID"],
                    "CompanyName": supplier["CompanyName"],
                    "Status": "FAIL",
                    "Reasons": errors
                })

        # Requested count validation

        if len(valid_suppliers) < requirement.requested_results:

            report.append({
                "SupplierID": "-",
                "CompanyName": "-",
                "Status": "WARNING",
                "Reasons": [
                    f"Only {len(valid_suppliers)} valid suppliers found."
                ]
            })

        return valid_suppliers, report