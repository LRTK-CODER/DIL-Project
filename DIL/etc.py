import pandas
from .util import DataSetting

DataFrame = pandas.DataFrame


class Etc(DataSetting):
    def sampling(self, percent: int) -> DataFrame:
        datas = self.datas.loc[
            :,
        ].sample(n=len(self.datas) // percent)
        return datas

    def anatomization(self, identyColumn: str, currentColumnList: list) -> DataFrame:
        currentColumnList.insert(0, identyColumn)
        nonCurrentColumnList = list(set(list(self.datas)) - set(currentColumnList))
        nonCurrentColumnList.insert(0, identyColumn)

        return (
            self.datas.loc[:, currentColumnList],
            self.datas.loc[:, nonCurrentColumnList],
        )
