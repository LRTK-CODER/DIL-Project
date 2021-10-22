import pandas, pytest
from DIL import crypto


@pytest.fixture
def ope_fixture(datas_fixture):
    key = "testcode"
    dataSetting = crypto.OPECipher(datas_fixture, key=key)

    return dataSetting


class TestOPE:
    @pytest.fixture(autouse=True)
    def _opeInit(self, ope_fixture):
        self._ope = ope_fixture

    def test_encrypt(self):
        original = self._ope.datas.copy()

        self._ope.encrypt("나이")
        encrypt_values = self._ope.datas

        assert not encrypt_values.equals(original["나이"])

    def test_decrypt(self):
        original = self._ope.datas.copy()

        # 암호화
        self._ope.encrypt("나이")

        # 복호화
        self._ope.decrypt("나이")
        decrypt_values = self._ope.datas

        for original_value, decrypt_value in zip(original, decrypt_values):
            assert original_value == decrypt_value
