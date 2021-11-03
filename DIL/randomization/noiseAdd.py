import random
from util import DataSetting


class Noise(DataSetting):
    """
    | 무작위화 기술 중 잡음추가 기술을 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.
    """

    def init(self, datas):
        super().init(datas)

    def add(self, column: str, randomRange: list = [-9, 9]):
        """
        잡음추가 기술 중 잡음을 더하는 메소드

        Parameters
        ----------
        column : str
            잡음 추가 기술을 적용할 컬럼
        randomRange : list
            잡음 추가 기술에 사용될 잡음의 범위

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        datas = self.toList(column)
        result = [
            data + random.randrange(randomRange[0], randomRange[1]) for data in datas
        ]

        self.datas[column] = result
        return True

    def multipleAdd(self, columns: list, randomRange: list = [-9, 9]):
        """
        잡음추가 기술 중 잡음을 곱하는 메소드

        Parameters
        ----------
        columns : list
            잡음 추가 기술을 적용할 컬럼들
        randomRange : list
            잡음 추가 기술에 사용될 잡음의 범위

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        noiseList = [
            random.randrange(randomRange[0], randomRange[1])
            for _ in range(0, len(self.datas))
        ]
        for idx, noise in enumerate(noiseList):
            for column in columns:
                self.datas.at[idx, column] += noise

        return True
