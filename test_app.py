from app import get_system_status


def test_system_status():
    result = get_system_status()

    assert result["status"] == "FAILED"
    assert result["application"] == "Infrastructure Health API"
    assert result["version"] == "1.0.0"


def test_required_fields_exist():
    result = get_system_status()

    assert "status" in result
    assert "application" in result
    assert "version" in result
    assert "platform" in result
    assert "timestamp" in result
