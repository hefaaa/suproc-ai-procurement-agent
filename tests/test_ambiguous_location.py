from agent.parser import RequirementParser


def test_ambiguous_location():

    parser = RequirementParser()

    requirement = parser.parse(
        "Find suppliers in South India."
    )

    assert len(requirement.locations) > 0