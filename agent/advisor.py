import json
import ollama


class LLMAdvisor:

    def __init__(self):
        self.model = "qwen3:1.7b"

    def generate_analysis(self, requirement, suppliers):

        supplier_names = []

        for supplier in suppliers:
            supplier_names.append(supplier["CompanyName"])

        prompt = f"""
You are an AI Procurement Advisor.

Business Requirement

Objective:
{requirement.objective}

Category:
{requirement.category}

Selected Suppliers:
{", ".join(supplier_names)}

Return ONLY valid JSON.

{{
    "execution_plan":[
        "",
        "",
        "",
        "",
        "",
        ""
    ],

    "missing_information":[
        "",
        "",
        ""
    ],

    "risks":[
        "",
        "",
        ""
    ],

    "outreach":""
}}
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content":
                    "Return ONLY valid JSON. Do not explain."
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

        return json.loads(output)