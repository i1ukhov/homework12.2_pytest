from utils.dicts import get_val


def test_get_val():
    assert get_val({"key": "value"}, "key", "git") == "value"
    assert get_val({"Sarah": "Connor"}, "Sarah", "git") == "Connor"
    assert get_val({}, None, "git") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"
    assert get_val([], "g") == "git"
    assert get_val({"l": "L"}, "k") == "git"