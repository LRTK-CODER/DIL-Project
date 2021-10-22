from .util import DataSetting


class Generalization(DataSetting):
    def local(self, column: str, currentIndexList: list) -> None:
        datas = self.datas.loc[currentIndexList[0] : currentIndexList[1], column]
        self.datas.loc[currentIndexList[0] : currentIndexList[1], column] = [
            f"{min(datas)} ~ {max(datas)}" for _ in datas
        ]

    def categorizion(self, column: str, replaceList: list, category: str) -> None:
        datas = self._toList(column)
        result = [category if data in replaceList else data for data in datas]
        self.datas.loc[:, column] = result
