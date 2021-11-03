import pytest
from DIL import statistics


@pytest.fixture
def aggregation_fixture(datas_fixture):
    dataSetting = statistics.Aggregation(datas_fixture.copy())

    return dataSetting


class TestAggregation:
    @pytest.fixture(autouse=True)
    def _aggregationInit(self, aggregation_fixture):
        self._aggregation = aggregation_fixture

    def test_mean(self):
        self._aggregation.mean("나이")
        mean_value = self._aggregation.datas["나이"]

        for value in mean_value:
            assert value == 46

    def test_max(self):
        self._aggregation.max("나이")
        max_value = self._aggregation.datas["나이"]

        for value in max_value:
            assert value == 70

    def test_min(self):
        self._aggregation.min("나이")
        min_value = self._aggregation.datas["나이"]

        for value in min_value:
            assert value == 20

    def test_mode(self):
        self._aggregation.mode("나이")
        mode_value = self._aggregation.datas["나이"]

        for value in mode_value:
            assert value == 66

    def test_median(self):
        self._aggregation.median("나이")
        median_value = self._aggregation.datas["나이"]

        # I think 45 is median value from the fixture field '나이'
        for value in median_value:
            assert value == 45
