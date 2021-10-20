import pytest, os


@pytest.fixture
def path_fixture():
    CURRENT_DIR_PATH = os.path.dirname(__file__)
    TEST_FIXTURE_REL_PATH = "../Sample/test_100.csv"
    TEST_FIXTURE_PATH = os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)

    return TEST_FIXTURE_REL_PATH
