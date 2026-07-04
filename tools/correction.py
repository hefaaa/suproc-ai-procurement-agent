class CorrectionTool:

    def correct(self, suppliers, report, requirement):

        correction_report = []

        passed = [
            item for item in report
            if item["Status"] == "PASS"
        ]

        failed = [
            item for item in report
            if item["Status"] == "FAIL"
        ]

        if failed:
            correction_report.append(
                f"{len(failed)} supplier(s) failed validation."
            )

        if len(suppliers) < requirement.requested_results:
            correction_report.append(
                f"Only {len(suppliers)} valid supplier(s) available. Requested {requirement.requested_results}."
            )

        if not correction_report:
            correction_report.append(
                "No correction required."
            )

        return suppliers, correction_report