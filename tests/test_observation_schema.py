from kana.collector import collect_manual
from kana.observation_schema import new_observation, validate_observation_shape


def test_new_observation_is_valid() -> None:
    data = new_observation("001-hoso", ".hoso", content="example")
    assert validate_observation_shape(data) == []


def test_missing_required_field_is_reported() -> None:
    data = collect_manual("001-hoso", ".hoso", "example")
    del data["command"]
    assert "missing required field: command" in validate_observation_shape(data)


def test_invalid_schema_version_is_reported() -> None:
    data = new_observation("001-hoso", ".hoso")
    data["schema_version"] = 999
    assert validate_observation_shape(data)
