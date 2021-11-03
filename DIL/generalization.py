from .util import DataSetting


class Generalization(DataSetting):
    """
    | 일반화 기술 중 로컬 일반화, 문자데이터 범주화를 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.
    """

    def local(self, column: str, currentIndexList: list):
        """
        일반화 기술 중 로컬 일반화를 수행하는 함수

        Parameters
        ----------
        column : str
            로컬 일반화를 적용할 컬럼
        currentIndexList : list
            로컬 일반화를 적용할 Index 범위

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        datas = self.datas.loc[currentIndexList[0] : currentIndexList[1], column]
        self.datas.loc[currentIndexList[0] : currentIndexList[1], column] = [
            f"{min(datas)} ~ {max(datas)}" for _ in datas
        ]

        return True

    def categorizion(self, column: str, replaceList: list, category: str):
        """
        일반화 기술 중 문자데이터 범주화를 수행하는 함수

        Parameters
        ----------
        column : str
            문자데이터 범주화를 적용할 컬럼
        replaceList : list
            범주화로 치환될 문자 데이터 목록
        category : str
            범주화로 치환할 문자 데이터

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        datas = self._toList(column)
        result = [category if data in replaceList else data for data in datas]
        self.datas.loc[:, column] = result

        return True
