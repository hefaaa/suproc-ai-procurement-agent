class FilterTool:

    def filter_by_constraints(
        self,
        suppliers,
        min_capacity=None,
        max_delivery_days=None,
        certification=None,
        availability=None
    ):

        filtered = []

        for supplier in suppliers:

            if min_capacity is not None:

                if supplier["Capacity"] < min_capacity:
                    continue

            if max_delivery_days is not None:

                if max_delivery_days > 0 and supplier["DeliveryDays"] > max_delivery_days:
                    continue

            if certification:

                if supplier["Certification"] != certification:
                    continue

            if availability:

                if supplier["Availability"] != availability:
                    continue

            filtered.append(supplier)

        return filtered