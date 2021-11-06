import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import random, numpy as np, pandas
from util import DataSetting


class Permutation(DataSetting):
    """
    | 무작위화 기술 중 순열(재정렬) 기술을 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.

    Parameters
    ----------
        - datas : pandas.DataFrame
            순열 기술을 적용할 DataFrame 지정
    """

    def all(self, column: str):
        """
        순열을 구현한 메소드로 한가지 컬럼의 모든 데이터의 순서를 재정렬하는 메소드

        Parameters
        ----------
            - column : str
                순열 기술을 적용할 컬럼

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
        datas = self.datas.loc[:, [column]]
        shuttleDatas = datas.sample(frac=1).reset_index(drop=True)

        self.datas[column] = shuttleDatas
        return True
