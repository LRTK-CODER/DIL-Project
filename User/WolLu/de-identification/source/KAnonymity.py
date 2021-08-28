import pandas

dataFrame = pandas.core.frame.DataFrame

# K 익명성 메인 함수
def kAnonymity(df: dataFrame, indexSize: int, exceptionColumns: list = []):
    '''
    Creator: 정재윤
    Create Date: 2021.08.14
    Last Modified Date: 2021.08.14
    Version: 1.0
    Support Type: NULL

    [Explanation]
    이 함수는 exceptionColumns 퀄럼 외의 모든 퀄럼의 K-익명성 여부를 검사하여 출력하여 준다.

    [Parameter]
    exceptionColumns : 해당 리스트 안에 명시된 퀄럼은 K-익명성 검사에서 제외한다.
    '''

    columns = list(df.columns)
    kDict = {}

    for columnName in columns:
        if columnName in exceptionColumns: continue
        kDict[columnName] = getOccurrenceCount(df, indexSize, columnName)

    return kDict

def getOccurrenceCount(df: dataFrame, indexSize: int, columnName: str = ''):
    new_list = {}
    for i in range(0, indexSize):
        try: new_list[df.loc[i, columnName]] += 1
        except: new_list[df.loc[i, columnName]] = 1

    return new_list