import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pytest
from DIL import Etc


@pytest.fixture
def etc_fixture(datas_fixture):
    dataSetting = Etc(datas_fixture.copy())

    return dataSetting


class TestEtc:
    @pytest.fixture(autouse=True)
    def _etcInit(self, etc_fixture):
        self._etc = etc_fixture

    @pytest.mark.parametrize(
        "length",
        [10, 20, 11, 15, 1, 2],
    )
    def test_sampling(self, length):
        assert (len(self._etc.datas) // length) == len(self._etc.sampling(length))

    def test_anatomization(self):
        identyColumn = "회원번호"
        identyColumnList = ["이름", "성별", "주소"]

        identy, nonIdenty = self._etc.anatomization(
            identyColumn="회원번호", currentColumnList=["이름", "성별", "주소"]
        )

        checkNonIdentyColumnList = set(self._etc.datas)

        assert sorted(list(nonIdenty)) == sorted(
            list(checkNonIdentyColumnList - set(identyColumnList))
        )
