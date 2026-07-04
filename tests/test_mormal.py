from agent.parser import RequirementParser
from agent.executor import AgentExecutor


def test_normal_request():

    parser = RequirementParser()
    executor = AgentExecutor()

    requirement = parser.parse(
        "Find three biodegradable suppliers from South India."
    )

    result = executor.execute(requirement)

    assert len(result["recommendations"]) > 0