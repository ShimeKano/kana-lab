from kana.parser import observation_from_message


def test_observation_preserves_non_sensitive_response_data() -> None:
    observation = observation_from_message(
        ".danhboss",
        "Boss đang xuất hiện",
        metadata={"response_type": "message"},
    )

    assert observation.action == ".danhboss"
    assert observation.content == "Boss đang xuất hiện"
    assert observation.metadata["response_type"] == "message"
