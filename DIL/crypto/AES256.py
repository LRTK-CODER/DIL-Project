import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, hashlib, base64
from Crypto import Random
from Crypto.Cipher import AES

from util import DataSetting

DataFrame = pandas.DataFrame


class AES256(DataSetting):
    def __init__(self, datas: DataFrame, key):
        self.datas = datas

        self.bs = 32
        self.key = hashlib.sha256(key.encode("utf-8")).digest()

    def encrypt(self, column: str):
        datas = self._toList(column)

        result = []
        for raw in datas:
            raw = self._pad(raw)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            cipherText = base64.b64encode(iv + cipher.encrypt(raw.encode()))
            result.append(cipherText.decode())

        self.datas.loc[:, column] = result

    def decrypt(self, column: str):
        datas = self._toList(column)

        result = []
        for enc in datas:
            enc = base64.b64decode(enc.encode())
            iv = enc[: AES.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            plainText = self._unpad(cipher.decrypt(enc[AES.block_size :])).decode(
                "utf-8"
            )
            result.append(plainText)

        self.datas.loc[:, column] = result

    def _pad(self, s):
        return s + (self.bs - len(s.encode("utf-8")) % self.bs) * chr(
            self.bs - len(s.encode("utf-8")) % self.bs
        )

    @staticmethod
    def _unpad(s):
        return s[: -s[-1]]


if __name__ == "__main__":
    excel = pandas.read_csv("../Sample/test_100.csv", index_col=0)
    print(excel.head())

    AES256(excel, "test").encrypt("이름")
    print(excel.head())

    AES256(excel, "test").decrypt("이름")
    print(excel.head())
