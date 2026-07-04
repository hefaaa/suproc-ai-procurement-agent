class Corrector:

    def retry(self, executor, requirement, max_attempts=3):

        for attempt in range(1, max_attempts + 1):

            print(f"\nCorrection Attempt {attempt}")

            result = executor.execute(requirement)

            valid = result["recommendations"]

            report = result["validation_report"]

            has_fail = any(
                item["Status"] == "FAIL"
                for item in report
            )

            if not has_fail:
                return result

        print("\nMaximum correction attempts reached.")

        return result