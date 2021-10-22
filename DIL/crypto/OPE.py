import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from pyope.ope import OPE, ValueRange

from util import DataSetting

DataFrame = pandas.DataFrame


class OPECipher(DataSetting):
    def __init__(self, datas: DataFrame, key: str):
        self.datas = datas
        self.cipher = OPE(
            (key * 2).encode(),
            in_range=ValueRange(-10000, 10000),
            out_range=ValueRange(0, 1000000),
        )

    def encrypt(self, column: str):
        datas = self._toList(column)

        result = [self.cipher.encrypt(data) for data in datas]
        self.datas.loc[:, column] = result

    def decrypt(self, column: str):
        datas = self._toList(column)

        result = [self.cipher.decrypt(data) for data in datas]
        self.datas.loc[:, column] = result
