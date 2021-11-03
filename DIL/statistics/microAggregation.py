import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util import DataSetting


class MicroAggregation(DataSetting):
    """
    | 통계 기술 중 부분 총계 기술(평균값, 최댓값, 최솟값, 최빈값, 중간값)을 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.
    """

    def mean(self, column: str, currentIndex: int):
        """
        부분 총계 기술의 평균값을 구현한 메소드

        Parameters
        ----------
        column : str
            부분 총계 기술의 평균값을 적용할 컬럼
        currentIndex : int
            부분 총계 기술의 평균값을 적용할 Index

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        meanValue = int(self.datas[column].mean())
        self.datas.at[currentIndex, column] = meanValue

        return True

    def max(self, column: str, currentIndex: int):
        """
        부분 총계 기술의 최댓값을 구현한 메소드

        Parameters
        ----------
        column : str
            부분 총계 기술의 최댓값을 적용할 컬럼
        currentIndex : int
            부분 총계 기술의 최댓값을 적용할 Index

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        maxValue = self.datas[column].max()
        self.datas.at[currentIndex, column] = maxValue

        return True

    def min(self, column: str, currentIndex: int):
        """
        부분 총계 기술의 최솟값을 구현한 메소드

        Parameters
        ----------
        column : str
            부분 총계 기술의 최솟값을 적용할 컬럼
        currentIndex : int
            부분 총계 기술의 최솟값을 적용할 Index

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        minValue = self.datas[column].min()
        self.datas.at[currentIndex, column] = minValue

        return True

    def mode(self, column: str, currentIndex: int):
        """
        부분 총계 기술의 최빈값을 구현한 메소드

        Parameters
        ----------
        column : str
            부분 총계 기술의 최빈값을 적용할 컬럼
        currentIndex : int
            부분 총계 기술의 최빈값을 적용할 Index

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        modeValue = list(self.datas[column].mode())[-1]
        self.datas.at[currentIndex, column] = modeValue

        return True

    def median(self, column: str, currentIndex: int):
        """
        부분 총계 기술의 중간값을 구현한 메소드

        Parameters
        ----------
        column : str
            부분 총계 기술의 중간값을 적용할 컬럼
        currentIndex : int
            부분 총계 기술의 중간값을 적용할 Index

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        medianValue = int(self.datas[column].median())
        self.datas.at[currentIndex, column] = medianValue

        return True
