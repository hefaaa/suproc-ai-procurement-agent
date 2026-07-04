from agent.parser import RequirementParser


def test_missing_request_info():

    parser = RequirementParser()

    requirement = parser.parse(
        "Need suppliers."
    )

    assert requirement.entity_type == "supplier"