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

    @pytest.mark.parametrize('column, currentIndex, result', [
        ('나이', 0, 46),
        ('나이', 4, 46),
        ('나이', 10, 46),
        ('나이', 23, 46),
        ('나이', 53, 46)
    ])
    def test_mean(self, column, currentIndex, result):
        mean_value = self._microAggregation.mean(column, currentIndex)
        
        assert mean_value == result

    @pytest.mark.parametrize('column, currentIndex, result', [
        ('나이', 0, 70),
        ('나이', 4, 70),
        ('나이', 10, 70),
        ('나이', 23, 70),
        ('나이', 53, 70)
    ])
    def test_max(self, column, currentIndex, result):
        max_value = self._microAggregation.max(column, currentIndex)
        
        assert max_value == result

    @pytest.mark.parametrize('column, currentIndex, result', [
        ('나이', 0, 20),
        ('나이', 4, 20),
        ('나이', 10, 20),
        ('나이', 23, 20),
        ('나이', 53, 20)
    ])
    def test_min(self, column, currentIndex, result):
        min_value = self._microAggregation.min(column, currentIndex)
        
        assert min_value == result

    @pytest.mark.parametrize('column, currentIndex, result', [
        ('나이', 0, 66),
        ('나이', 4, 66),
        ('나이', 10, 66),
        ('나이', 23, 66),
        ('나이', 53, 66)
    ])
    def test_mode(self, column, currentIndex, result):
        mode_value = self._microAggregation.mode(column, currentIndex)
        
        assert mode_value == result

    @pytest.mark.parametrize('column, currentIndex, result', [
        ('나이', 0, 45),
        ('나이', 4, 45),
        ('나이', 10, 45),
        ('나이', 23, 45),
        ('나이', 53, 45)
    ])
    def test_median(self, column, currentIndex, result):
        median_value = self._microAggregation.median(column, currentIndex)

        assert median_value == result