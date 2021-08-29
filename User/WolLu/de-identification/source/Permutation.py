import pandas
import random

dataFrame = pandas.core.frame.DataFrame

class Permutation:
    @staticmethod
    def permutation(df: dataFrame, indexSize: int, columnName: str):
        '''
            Creator: 정재윤
            Create Date: 2021.08.29
            Last Modified Date: 2021.08.29
            Version: 1.0
            Support Type: NULL

            [Explanation]
            이 함수는 columnName 퀄럼의 모든 레코드의 순서를 뒤섞어 배치한다.

            [Parameter]
            setColumn : 동질집합으로 사용할 퀄럼 이름을 받는다.
        '''

        lst = list(df.loc[:, columnName])
        random.shuffle(lst)

        df.loc[:, columnName] = lst

        return True