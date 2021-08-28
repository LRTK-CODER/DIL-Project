import pandas
import numpy
from scipy import stats

dataFrame = pandas.core.frame.DataFrame

# 평균값 총계처리
def meanAggregation(df: dataFrame, indexSize: int, columnName: str, start: int = 0, end: int = 0, isRound:bool = False):
    '''
    Creator: 정재윤
    Create Date: 2021.07.09
    Last Modified Date: 2021.08.20
    Version: 2.2
    Support Type: Int, Float
  
    [Explanation]
    이 함수는 columnName 이름의 행의 start 부터 end까지의 데이터를 평균값으로 총계처리하여
    원본 DataFrame에 적용하는 역할을 수행한다.
 
    [Parameter]
    start : 부분총계를 진행할때 시작 index값
    end : 부분총계를 진행할때 종료 index값, 0 또는 indexSize값 초과시 indexSize로 설정
    isRound : True = 결과값 반올림, False = 결과값 유지
    '''
    
    result = 0

    if end == 0 or end > indexSize:
        end = indexSize

    for i in range(start, end):
        result += df.loc[i, columnName]

    result /= (end - start)

    if(isRound == True):
        result = round(result)

    for i in range(start, end):
        df.loc[i, columnName] = result

    return True

# 최대값 총계처리
def maxAggregation(df: dataFrame, indexSize: int, columnName: str, start: int = 0, end: int = 0):
    '''
        Creator: 정재윤
        Create Date: 2021.07.09
        Last Modified Date: 2021.08.20
        Version: 2.1
        Support Type: Int, Float

        [Explanation]
        이 함수는 columnName 이름의 행의 start 부터 end까지의 데이터를 최대값으로 총계처리하여
        원본 DataFrame에 적용하는 역할을 수행한다.

        [Parameter]
        start : 부분총계를 진행할때 시작 index값
        end : 부분총계를 진행할때 종료 index값, 0 또는 indexSize값 초과시 indexSize로 설정
    '''

    result = df.loc[start, columnName]

    if end == 0 or end > indexSize:
        end = indexSize

    for i in range(start, end):
        data = df.loc[i, columnName]

        if(data > result):
            result = data

    for i in range(start, end):
        df.loc[i, columnName] = result

    return True

# 최소값 총계처리
def minAggregation(df: dataFrame, indexSize: int, columnName: str, start: int = 0, end: int = 0):
    '''
        Creator: 정재윤
        Create Date: 2021.07.09
        Last Modified Date: 2021.08.20
        Version: 1.1
        Support Type: Int, Float

        [Explanation]
        이 함수는 columnName 이름의 행의 start 부터 end까지의 데이터를 최소값으로 총계처리하여
        원본 DataFrame에 적용하는 역할을 수행한다.

        [Parameter]
        start : 부분총계를 진행할때 시작 index값
        end : 부분총계를 진행할때 종료 index값, 0 또는 indexSize값 초과시 indexSize로 설정
    '''

    result = df.loc[start, columnName]

    if end == 0 or end > indexSize:
        end = indexSize

    for i in range(start, end):
        data = df.loc[i, columnName]
        if(data < result):
            result = data

    for i in range(start, end):
        df.loc[i, columnName] = result

    return True

# 중앙값 총계처리
def midAggregation(df: dataFrame, indexSize: int, columnName: str, start: int = 0, end: int = 0):
    '''
        Creator: 정재윤
        Create Date: 2021.07.09
        Last Modified Date: 2021.08.20
        Version: 1.1
        Support Type: Int, Float

        [Explanation]
        이 함수는 columnName 이름의 행의 start 부터 end까지의 데이터를 중앙값으로 총계처리하여
        원본 DataFrame에 적용하는 역할을 수행한다.
    '''
    datas = list(df.loc[start:end, columnName])

    result = numpy.median(datas)

    if end == 0 or end > indexSize:
        end = indexSize

    for i in range(start, end):
        df.loc[i, columnName] = result

    return True

# 최빈값 총계처리
def modeAggregation(df: dataFrame, indexSize: int, columnName: str, start: int = 0, end: int = 0):
    '''
        Creator: 정재윤
        Create Date: 2021.07.09
        Last Modified Date: 2021.08.20
        Version: 1.1
        Support Type: Int, Float

        [Explanation]
        이 함수는 columnName 이름의 행의 start 부터 end까지의 데이터를 최빈값으로 총계처리하여
        원본 DataFrame에 적용하는 역할을 수행한다.
    '''

    if end == 0 or end > indexSize:
        end = indexSize

    datas = list(df.loc[start:end, columnName])

    result = stats.mode(datas)[0]

    for i in range(start, end):
        df.loc[i, columnName] = result

    return True