import pandas
from .util import DataSetting

DataFrame = pandas.DataFrame


class Etc(DataSetting):
    """
    기타 기술(표본추출, 해부화)을 구현한 클래스
    """

    def sampling(self, percent: int) -> DataFrame:
        """
        기타 기술 중 표본추출을 수행하는 메소드

        Parameters
        ----------
        percent : int
            표본추출 퍼센트

        Returns
        -------
        datas
            표본추출 기술이 적용된 데이터를 리턴
        """
        datas = self.datas.loc[
            :,
        ].sample(n=len(self.datas) // percent)
        return datas

    def anatomization(self, identyColumn: str, currentColumnList: list) -> DataFrame:
        """
        기타 기술 중 해부화를 수행하는 메소드

        Parameters
        ----------
        identyColumn : str
            식별 컬럼

        currentColumnList: list
        |    식별 가능한 컬럼들

        Returns
        -------
        Tuple type data
            | Tuple 타입의 첫번째 데이터 : 식별 가능한 컬럼만 있는 DataFrame
            | Tuple 타입의 두번째 데이터 : 민감데이터 컬럼와 식별 컬럼이 있는 DataFrame
        """
        currentColumnList.insert(0, identyColumn)
        nonCurrentColumnList = list(set(list(self.datas)) - set(currentColumnList))
        nonCurrentColumnList.insert(0, identyColumn)

        return (
            self.datas.loc[:, currentColumnList],
            self.datas.loc[:, nonCurrentColumnList],
        )
