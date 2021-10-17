import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pytest
from DIL import statistics

# 경로 설정
CURRENT_DIR_PATH=os.path.dirname(__file__)
TEST_FIXTURE_REL_PATH="../Sample/test_100.csv"
TEST_FIXTURE_PATH=os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)

@pytest.fixture
def microAggregation_fixture():
    excel = pandas.read_csv(TEST_FIXTURE_PATH, index_col=0)
    dataSetting = statistics.MicroAggregation(excel)
    
    return dataSetting

class TestMicroAggregation:
    @pytest.fixture(autouse=True)
    def _microAggregationInit(self, microAggregation_fixture):
        self._microAggregation = microAggregation_fixture

    def test_mean(self):
        mean_value = self._microAggregation.mean('나이', currentIndex=0)
        
        assert mean_value == 46

    def test_max(self):
        max_value = self._microAggregation.max('나이', currentIndex=0)
        
        assert max_value == 70

    def test_median(self):
        median_value = self._microAggregation.median('나이', currentIndex=0)

        assert median_value == 45