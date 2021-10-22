import pandas, pytest
from DIL import Generalization


@pytest.fixture
def eneralization_fixture(datas_fixture):
    dataSetting = Generalization(datas_fixture.copy())

    return dataSetting


class TestGeneralization:
    @pytest.fixture(autouse=True)
    def _generalizationInit(self, eneralization_fixture):
        self._eneralization = eneralization_fixture

    @pytest.mark.parametrize(
        "local_scope",
        [
            [0, 3],
            [1, 4],
            [5, 100],
            [2, 3],
            [20, 30],
        ],
    )
    def test_local_target(self, local_scope):
        targetColumn = "성별"
        self._eneralization.local(column=targetColumn, currentIndexList=local_scope)

        local_values = self._eneralization.datas
        for value in local_values[targetColumn][local_scope[0] : local_scope[1] + 1]:
            assert value == "남성 ~ 여성"

    @pytest.mark.parametrize(
        "local_scope",
        [
            [0, 3],
            [1, 4],
            [5, 100],
            [2, 3],
            [20, 30],
        ],
    )
    def test_local_non_target(self, local_scope):
        targetColumn = "성별"
        self._eneralization.local(column=targetColumn, currentIndexList=local_scope)

        local_values = self._eneralization.datas
        for value in local_values[targetColumn][local_scope[1] + 1 :]:
            assert value != "남성 ~ 여성"


# 문자데이터 범주화
# genTest.categorizion(column="성별", replaceList=["남성", "여성"], category="Gender")

# print(excel.head())
