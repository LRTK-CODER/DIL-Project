import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pytest
from DIL import randomization

# 경로 설정
CURRENT_DIR_PATH=os.path.dirname(__file__)
TEST_FIXTURE_REL_PATH="../Sample/test_100.csv"
TEST_FIXTURE_PATH=os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)

@pytest.fixture
def permutation_fixture():
    excel = pandas.read_csv(TEST_FIXTURE_PATH, index_col=0)
    dataSetting = randomization.Permutation(excel.copy())
    
    return dataSetting

class TestPermutation:
    @pytest.fixture(autouse=True)
    def _permutationInit(self, permutation_fixture):
        self._permutation = permutation_fixture

    def test_dataSetting(self):
        assert type(self._permutation.datas) is pandas.DataFrame

    def test_all(self):
        permutation_value = self._permutation.all('나이')
        excel = pandas.read_csv(TEST_FIXTURE_PATH, index_col=0)

        assert not permutation_value.equals(excel['나이'])