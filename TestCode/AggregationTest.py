import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pytest
from DIL import statistics

# 경로 설정
CURRENT_DIR_PATH=os.path.dirname(__file__)
TEST_FIXTURE_REL_PATH="../Sample/test_100.csv"
TEST_FIXTURE_PATH=os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)

@pytest.fixture
def aggregation_fixture():
    excel = pandas.read_csv(TEST_FIXTURE_PATH, index_col=0)
    dataSetting = statistics.Aggregation(excel.copy())
    
    return dataSetting

class TestAggregation:
    @pytest.fixture(autouse=True)
    def _aggregationInit(self, aggregation_fixture):
        self._aggregation = aggregation_fixture

    def test_mean(self):
        mean_value = self._aggregation.mean('나이')

        for value in mean_value:
            assert value == 46
    
    def test_max(self):
        max_value = self._aggregation.max('나이')

        for value in max_value:
            assert value == 70

    def test_min(self):
        min_value = self._aggregation.min('나이')

        for value in min_value:
            assert value == 20

    def test_mode(self):
        mode_value = self._aggregation.mode('나이')

        for value in mode_value:
            assert value == 66

    def test_median(self):
        median_value = self._aggregation.median('나이')

        # I think 45 is median value from the fixture field '나이'
        for value in median_value:
            assert value == 45