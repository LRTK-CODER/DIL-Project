import pandas

dataFrame = pandas.core.frame.DataFrame

# L 다양성 메인 함수
def lDiversity(df: dataFrame, setColumn: str, checkColumn: str):
    '''
    Creator: 정재윤
    Create Date: 2021.08.20
    Last Modified Date: 2021.08.20
    Version: 1.0
    Support Type: NULL

    [Explanation]
    이 함수는 동질집합(setColumn)의 각각의 집합안에 checkColumn의 L-다양성 값을 산출하여 Dictionary 형태로 반환한다.

    [Parameter]
    setColumn : 동질집합으로 사용할 퀄럼 이름을 받는다.
    checkColumn : 실제로 L-다양성 검사를 진행할 퀄럼 이름을 받는다.
    '''

    setDict = getColumnSet(df.loc[:, setColumn])
    lDict = {}

    for i in setDict:
        lst = []
        for j in setDict[i]: lst.append(df.loc[j, checkColumn])
        lDict[i] = len(set(lst))

    return lDict

def getColumnSet(column: list):
    result = {}

    for data in set(column):
        lst = []
        for i in range(0, len(column)):
            if column[i] != data: continue
            lst.append(i)
        result[data] = lst

    return result