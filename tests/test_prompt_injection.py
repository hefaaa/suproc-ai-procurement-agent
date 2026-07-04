from agent.executor import AgentExecutor
from agent.parser import RequirementParser


def test_prompt_injection():

    parser = RequirementParser()
    executor = AgentExecutor()

    requirement = parser.parse(
        "Find biodegradable suppliers"
    )

    result = executor.execute(requirement)

    report = result["validation_report"]

    injection_detected = any(
        item["Status"] == "FAIL" and
        any(
            "Prompt injection" in reason
            for reason in item.get("Reasons", [])
        )
        for item in report
    )

    assert injection_detected