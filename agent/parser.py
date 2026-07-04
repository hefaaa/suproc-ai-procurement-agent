import re
import json
import ollama

from models.schemas import Requirement


class RequirementParser:

    def __init__(self):
        self.model = "qwen3:1.7b"

    def parse(self, user_request):

        prompt = f"""
Return ONLY valid JSON.

Extract ONLY these fields.

{{
    "objective":"",
    "entity_type":"supplier",
    "preferences":{{}}
}}

Business Request:

{user_request}
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Return only JSON. No explanation."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        output = response["message"]["content"]

        output = output.replace("```json", "")
        output = output.replace("```", "")
        output = output.strip()

        data = json.loads(output)

        # -------------------------
        # Python extracts everything else
        # -------------------------

        request = user_request.lower()

        # Category

        if "biodegradable" in request:
            category = "Biodegradable Containers"

        elif "paper" in request:
            category = "Paper Containers"

        elif "plastic" in request:
            category = "Plastic Containers"

        elif "food" in request:
            category = "Food Containers"

        else:
            category = ""

        # Locations

        locations = []

        if "south india" in request:

            locations = [
                "Karnataka",
                "Tamil Nadu",
                "Kerala",
                "Andhra Pradesh",
                "Telangana"
            ]

        # Capacity

        capacity = 0

        match = re.search(r"(\d+)\s*units", request)

        if match:
            capacity = int(match.group(1))

        # Delivery

        delivery = 0

        match = re.search(r"(\d+)\s*days", request)

        if match:
            delivery = int(match.group(1))

        # Requested results

        requested = 3

        if "one" in request or "1" in request:
            requested = 1

        elif "two" in request or "2" in request:
            requested = 2

        elif "three" in request or "3" in request:
            requested = 3

        return Requirement(

            objective=data["objective"],

            entity_type="supplier",

            category=category,

            locations=locations,

            min_capacity=capacity,

            max_delivery_days=delivery,

            requested_results=requested,

            preferences=data.get("preferences", {})
        )