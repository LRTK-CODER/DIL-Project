def microAggregation(dataFrame:pandas.core.frame.DataFrame, indexSize : int, columnName: str, isRound = False):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

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