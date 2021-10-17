import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pytest
from DIL import statistics

# 경로 설정
CURRENT_DIR_PATH=os.path.dirname(__file__)
TEST_FIXTURE_REL_PATH="../Sample/test_100.csv"
TEST_FIXTURE_PATH=os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)

@pytest.fixture
def agrregation_fixture():
    excel = pandas.read_csv(TEST_FIXTURE_PATH, index_col=0)
    dataSetting = statistics.Aggregation(excel.copy())
    
    return dataSetting

class TestAggregation:
    @pytest.fixture(autouse=True)
    def _agrregationInit(self, agrregation_fixture):
        self._agrregation = agrregation_fixture

    def test_mean(self):
        mean_value = self._agrregation.mean('나이')

        for value in mean_value:
            assert value == 46

    def test_median(self):
        median_value = self._agrregation.median('나이')

        # I think 45 is median value from the fixture field '나이'
        for value in median_value:
            assert value == 45