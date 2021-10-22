import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import random
from util import DataSetting


class Noise(DataSetting):
    def __init__(self, datas):
        super().__init__(datas)

    def add(self, column: str, randomRange: list = [-9, 9]):
        datas = self._toList(column)
        result = [
            data + random.randrange(randomRange[0], randomRange[1]) for data in datas
        ]

        self.datas[column] = result
        return self.datas[column]

    def multipleAdd(self, columns: list, randomRange: list = [-9, 9]):
        noiseList = [
            random.randrange(randomRange[0], randomRange[1])
            for _ in range(0, len(self.datas))
        ]
        for idx, noise in enumerate(noiseList):
            for column in columns:
                self.datas.at[idx, column] += noise

        return self.datas[columns]
