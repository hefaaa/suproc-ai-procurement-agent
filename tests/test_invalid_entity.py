from agent.parser import RequirementParser


def test_invalid_entity():

    parser = RequirementParser()

    requirement = parser.parse(
        "Find doctors."
    )

    assert requirement is not None