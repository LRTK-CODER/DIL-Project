import pandas, pytest
from DIL import crypto


@pytest.fixture
def aes_fixture(datas_fixture):
    key = "testcode"
    dataSetting = crypto.AES256(datas_fixture, key)

    return dataSetting


class TestAES256:
    @pytest.fixture(autouse=True)
    def _aesInit(self, aes_fixture):
        self._aes = aes_fixture

    def test_encrypt(self):
        targetColumn = "전화번호"
        original = self._aes.datas.copy()

        # AES-256 암호화
        self._aes.encrypt("전화번호")
        encrypt_values = self._aes.datas["전화번호"]
        assert not encrypt_values.equals(original[targetColumn])

    def test_decrypt(self):
        targetColumn = "전화번호"
        original = self._aes.datas.copy()

        # AES-256 암호화
        self._aes.encrypt("전화번호")

        # AES-256 복호화
        self._aes.decrypt("전화번호")
        decrypt_values = self._aes.datas["전화번호"]
        assert self._aes.datas["전화번호"].equals(original[targetColumn])
