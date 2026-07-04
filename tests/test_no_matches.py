from agent.parser import RequirementParser
from agent.executor import AgentExecutor


def test_no_matches():

    parser = RequirementParser()
    executor = AgentExecutor()

    requirement = parser.parse(
        "Need suppliers with capacity 1000000 units."
    )

    result = executor.execute(requirement)

    assert len(result["recommendations"]) == 0