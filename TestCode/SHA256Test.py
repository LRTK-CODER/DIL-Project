import pandas, pytest
from DIL import crypto


@pytest.fixture
def sha_fixture(datas_fixture):
    dataSetting = crypto.hash.SHA256(datas_fixture)

    return dataSetting


class TestSHA256:
    @pytest.fixture(autouse=True)
    def _shaInit(self, sha_fixture):
        self._sha = sha_fixture

    @pytest.mark.parametrize(
        "column",
        ["이름", "성별", "생일", "전화번호", "주소"],
    )
    def test_encrypt(self, column):
        original_values = self._sha.datas[column]

        self._sha.run(column)
        encrypt_values = self._sha.datas[column]

        for original_value, encrypt_value in zip(original_values, encrypt_values):
            assert original_value == encrypt_value
