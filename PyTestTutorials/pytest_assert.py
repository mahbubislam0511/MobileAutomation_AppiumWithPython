import pytest


def test_validate_title():
    except_result = "google"
    actual_result = "bing"

    if actual_result == except_result:
        print("Test Pass")
        # assert True, "Test case pass"
        # assert actual_result == except_result
        assert except_result in actual_result
    else:
        print("Test Fail")
        assert False, "Test case fail"
