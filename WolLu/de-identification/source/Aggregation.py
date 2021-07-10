import pandas.core.frame
import numpy

# 평균값 총계처리(isRound : 반올림 여부 기본 False)
def meanAggregation(dataFrame: pandas.core.frame.DataFrame, indexSize: int, columnName: str, isRound = False):
    result = 0

    for i in range(indexSize):
        result += dataFrame.loc[i, columnName]

    result /= indexSize

    if(isRound == True):
        result = round(result)

    for i in range(indexSize):
        dataFrame.loc[i, columnName] = result

    return True

# 최대값 총계처리
def maxAggregation(dataFrame: pandas.core.frame.DataFrame, indexSize: int, columnName: str):
    result = dataFrame.loc[0, columnName]

    for i in range(indexSize):
        data = dataFrame.loc[i, columnName]

        if(data > result):
            result = data

    for i in range(indexSize):
        dataFrame.loc[i, columnName] = result

    return True

# 최소값 총계처리
def minAggregation(dataFrame: pandas.core.frame.DataFrame, indexSize: int, columnName: str):
    result = dataFrame.loc[0, columnName]

    for i in range(indexSize):
        data = dataFrame.loc[i, columnName]
        if(data < result):
            result = data

    for i in range(indexSize):
        dataFrame.loc[i, columnName] = result

    return True

# 중앙값 총계처리
def midAggregation(dataFrame: pandas.core.frame.DataFrame, indexSize: int, columnName: str):
    return True

# 최빈값 총계처리
def modeAggregation(dataFrame: pandas.core.frame.DataFrame, indexSize: int, columnName: str):
    return True

def microAggregation(dataFrame: pandas.core.frame.DataFrame, indexSize: int, columnName: str):
    std = list(dataFrame.loc[:, columnName])
    result = numpy.std(std)

    for i in range(indexSize):
        dataFrame.loc[i, columnName] = result

    return True