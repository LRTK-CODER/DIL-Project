import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas, pyffx

from util import DataSetting

DataFrame = pandas.DataFrame


class FPECipher(DataSetting):
    def __init__(
        self,
        datas: DataFrame,
        key: str,
        length: int,
        mode: str = int,
        alphabet: str = None,
    ):
        self.datas = datas
        self.key = key.encode()

        if mode == int:
            self.cipher = pyffx.Integer(self.key, length=length)
        elif mode == str:
            self.cipher = pyffx.String(self.key, alphabet=alphabet, length=length)

    def encrypt(self, column: str):
        datas = self._toList(column)
        result = [self.cipher.encrypt(data) for data in datas]

        self.datas.loc[:, column] = result

    def decrypt(self, column: str):
        datas = self._toList(column)
        result = [self.cipher.decrypt(data) for data in datas]

        self.datas.loc[:, column] = result
