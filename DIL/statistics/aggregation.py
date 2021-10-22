import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util import DataSetting


class Aggregation(DataSetting):
    def mean(self, column: str):
        meanValue = int(self.datas[column].mean())
        self.datas[column] = [meanValue] * len(self.datas)
        return self.datas[column]

    def max(self, column: str):
        maxValue = self.datas[column].max()
        self.datas[column] = [maxValue] * len(self.datas)
        return self.datas[column]

    def min(self, column: str):
        minValue = self.datas[column].min()
        self.datas[column] = [minValue] * len(self.datas)
        return self.datas[column]

    def mode(self, column: str):
        modeValue = list(self.datas[column].mode())[-1]
        self.datas[column] = [modeValue] * len(self.datas)
        return self.datas[column]

    def median(self, column: str):
        medianValue = int(self.datas[column].median())
        self.datas[column] = [medianValue] * len(self.datas)
        return self.datas[column]
