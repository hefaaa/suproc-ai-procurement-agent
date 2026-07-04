from agent.executor import AgentExecutor
from agent.parser import RequirementParser


def test_duplicate_records():

    parser = RequirementParser()
    executor = AgentExecutor()

    requirement = parser.parse(
        "Find suppliers."
    )

    result = executor.execute(requirement)

    ids = [
        s["SupplierID"]
        for s in result["recommendations"]
    ]

    assert len(ids) == len(set(ids))