import pytest


@pytest.fixture(scope="session", autouse=True)
def print_test_status():
    print("\n>>> Start testing")
    yield
    print("\n>>> Testing completed")


@pytest.fixture(autouse=True)
def run_before_after_tests():
    print("\nbefore test")
    yield
    print("\nafter test")
