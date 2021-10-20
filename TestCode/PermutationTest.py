import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pytest
from DIL import randomization


@pytest.fixture
def permutation_fixture(path_fixture):
    excel = pandas.read_csv(path_fixture, index_col=0)
    dataSetting = randomization.Permutation(excel.copy())

    return dataSetting


class TestPermutation:
    @pytest.fixture(autouse=True)
    def _permutationInit(self, permutation_fixture):
        self._permutation = permutation_fixture

    def test_dataSetting(self):
        assert type(self._permutation.datas) is pandas.DataFrame

    def test_all(self):
        permutation_value = self._permutation.all("나이")
        excel = pandas.read_csv("../Sample/test_100.csv", index_col=0)

        assert not permutation_value.equals(excel["나이"])
