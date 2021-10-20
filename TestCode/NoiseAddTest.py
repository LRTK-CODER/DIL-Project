import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pytest
from DIL import randomization


@pytest.fixture
def noise_fixture(path_fixture):
    excel = pandas.read_csv(path_fixture, index_col=0)
    dataSetting = randomization.Noise(excel)

    return dataSetting


class TestNoise:
    @pytest.fixture(autouse=True)
    def _noiseInit(self, noise_fixture):
        self._noise = noise_fixture

    def test_dataSetting(self):
        assert type(self._noise.datas) is pandas.DataFrame

    @pytest.mark.parametrize(
        "column, randomRange",
        [
            ("나이", [-9, 9]),
            ("나이", [-8, 9]),
            ("나이", [-8, 8]),
            ("나이", [-7, 8]),
        ],
    )
    def test_add(self, column, randomRange):
        noiseAdd_Value = self._noise.add(column, randomRange)
        assert not noiseAdd_Value.equals(noise_fixture)

    @pytest.mark.parametrize(
        "column, randomRange",
        [
            (["회원번호", "나이"], [-9, 9]),
            (["회원번호", "나이"], [-8, 9]),
            (["회원번호", "나이"], [-8, 8]),
            (["회원번호", "나이"], [-7, 8]),
        ],
    )
    def test_mulipleAdd(self, column, randomRange):
        noiseAdd_Value = self._noise.multipleAdd(column, randomRange)
        assert not noiseAdd_Value.equals(noise_fixture)
