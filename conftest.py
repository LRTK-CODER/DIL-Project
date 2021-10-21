import pytest, os, pandas

import DIL


@pytest.fixture
def datas_fixture():
    CURRENT_DIR_PATH = os.path.dirname(__file__)
    TEST_FIXTURE_REL_PATH = "./Sample/test_100.csv"
    TEST_FIXTURE_PATH = os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)

    datas = pandas.read_csv(TEST_FIXTURE_REL_PATH, index_col=0)
    return datas
