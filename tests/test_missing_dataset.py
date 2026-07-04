from agent.executor import AgentExecutor
from agent.parser import RequirementParser


def test_missing_dataset_info():

    parser = RequirementParser()
    executor = AgentExecutor()

    requirement = parser.parse(
        "Find biodegradable suppliers."
    )

    result = executor.execute(requirement)

    assert "validation_report" in result