import pandas
from pyope.ope import OPE, ValueRange

from util import DataSetting

DataFrame = pandas.DataFrame


class OPECipher(DataSetting):
    """
    | 암호화 기술 중 기타 암호화(순서보존)를 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.
    """

    def __init__(self, datas: DataFrame, key: str):
        self.datas = datas
        self.cipher = OPE(
            (key * 2).encode(),
            in_range=ValueRange(-10000, 10000),
            out_range=ValueRange(0, 1000000),
        )

    def encrypt(self, column: str):
        """
        순서보존 암호화를 수행하는 메소드

        Parameters
        ----------
        column : str
            순서보존 암호화를 적용할 컬럼

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        datas = self._toList(column)

        result = [self.cipher.encrypt(data) for data in datas]
        self.datas.loc[:, column] = result

        return True

    def decrypt(self, column: str):
        """
        순서보존 복호화를 수행하는 메소드

        Parameters
        ----------
        column : str
            순서보존 복호화를 적용할 컬럼

        Returns
        -------
        True
            기술 적용 성공 시 True 리턴
        """
        datas = self._toList(column)

        result = [self.cipher.decrypt(data) for data in datas]
        self.datas.loc[:, column] = result
