import pandas

DataFrame = pandas.DataFrame


class DataSetting:
    def __init__(self, datas: DataFrame):
        self.datas = datas

    def _toList(self, column: str):
        dataList = self.datas.loc[:, column]
        return list(dataList)
