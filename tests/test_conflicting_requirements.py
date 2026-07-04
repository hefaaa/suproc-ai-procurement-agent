from agent.parser import RequirementParser
from agent.executor import AgentExecutor


def test_conflicting_requirements():

    parser = RequirementParser()
    executor = AgentExecutor()

    requirement = parser.parse(
        "Need biodegradable suppliers delivering in 1 day with 500000 units."
    )

    result = executor.execute(requirement)

    report = result["validation_report"]

    assert any(
        item["Status"] != "PASS"
        for item in report
    )