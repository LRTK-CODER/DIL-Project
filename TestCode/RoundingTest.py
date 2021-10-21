import pytest
from DIL import Rounding


class TestRound:
    @pytest.mark.parametrize(
        "data, seatNum, result",
        [
            (4, 1, 0),
            (10, 1, 10),
            (25, 1, 30),
            (12, 1, 10),
            (49, 1, 50),
            (150, 2, 200),
            (141, 2, 100),
        ],
    )
    def test_off(self, data, seatNum, result):
        rounding_off_value = Rounding.off(data, seatNum)

        assert rounding_off_value == result

    @pytest.mark.parametrize(
        "data, seatNum, result",
        [
            (10, 1, 10),
            (25, 1, 30),
            (12, 1, 20),
            (49, 1, 50),
            (150, 2, 200),
            (141, 2, 200),
        ],
    )
    def test_up(self, data, seatNum, result):
        rounding_up_value = Rounding.up(data, seatNum)

        assert rounding_up_value == result

    @pytest.mark.parametrize(
        "data, seatNum, result",
        [
            (10, 1, 10),
            (25, 1, 20),
            (12, 1, 10),
            (49, 1, 40),
            (150, 2, 100),
            (141, 2, 100),
        ],
    )
    def test_down(self, data, seatNum, result):
        rounding_down_value = Rounding.down(data, seatNum)

        assert rounding_down_value == result

    def test_random(self, datas_fixture):
        datas = Rounding.random(datas_fixture, "나이")

        for data in datas:
            assert str(data)[-1] == "0"
