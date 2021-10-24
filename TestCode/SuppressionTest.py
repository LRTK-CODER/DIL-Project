import pandas, pytest
from DIL import Suppression


@pytest.fixture
def suppression_fixture(datas_fixture):
    dataSetting = Suppression(datas_fixture.copy())

    return dataSetting


class TestSuppression:
    @pytest.fixture(autouse=True)
    def _suppressionInit(self, suppression_fixture):
        self._suppression = suppression_fixture

    def test_general(self):
        origeralColumn = list(self._suppression.datas)
        currentColumn = ["전화번호", "주소"]

        self._suppression.general(["전화번호", "주소"])

        assert sorted(list(set(origeralColumn) - set(currentColumn))) == sorted(
            list(self._suppression.datas)
        )

    def test_partial(self):
        targetColumn = "이름"
        original = self._suppression.datas[targetColumn].copy()

        for original_value, partial_value in zip(
            original,
            self._suppression.partial(targetColumn, [1, 2]),
        ):
            assert original_value != partial_value

    @pytest.mark.parametrize(
        "currentIndexList",
        [
            ([0]),
            ([0, 2]),
            ([2, 6, 8]),
            ([10, 39, 70, 80]),
            ([10, 2, 70, 80, 99]),
            ([1, 0, 3, 10, 25, 56, 43]),
        ],
    )
    def test_record(self, currentIndexList):
        original_length = len(self._suppression.datas)
        delete_count = len(currentIndexList)

        record_values = self._suppression.record(currentIndexList)

        assert original_length - delete_count == len(record_values)

    @pytest.mark.parametrize(
        "column, currentIndexList",
        [
            ("이름", [0]),
            ("회원번호", [0, 2]),
            ("나이", [2, 6, 8]),
            ("생일", [10, 39, 70, 80]),
            ("전화번호", [10, 2, 70, 80, 99]),
            ("주소", [1, 0, 3, 10, 25, 56, 43]),
        ],
    )
    def test_local(self, column, currentIndexList):
        self._suppression.local(column, currentIndexList)
        for idx in currentIndexList:
            assert self._suppression.datas[column][idx] == ""

    def test_masking(self):
        targetColumn = "이름"
        masking_scope = [1, 3]

        masking_values = self._suppression.masking(targetColumn, masking_scope)

        for value in masking_values:
            assert value.count("*") == masking_scope[1] - masking_scope[0]

    def test_address_state(self):
        original = self._suppression.datas.copy()
        address_values = self._suppression.address("주소", 1)

        for original_value, address_value in zip(original, address_values):
            assert original_value != address_value

    def test_address_city(self):
        original = self._suppression.datas.copy()
        address_values = self._suppression.address("주소", 2)

        for original_value, address_value in zip(original, address_values):
            assert original_value != address_value
