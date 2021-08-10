import pandas, numpy

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

def roundOff(df:DataFrame, indexSize:int, columnName:str, seatNum:int) -> bool:
    if seatNum < 0:
        print('[Error] seatNum의 인자는 0를 초과해야합니다.')
        return False
    
    elif len(str(max(list(df.loc[:, columnName])))) < seatNum:
        print('[Error] 반올림을 할 자리가 잘못 입력되었습니다.')
        return False

    for index in range(indexSize):
        if not str(df.loc[index, columnName]).replace(',', '').isdigit():
            print('[Error] 숫자형 데이터가 아닙니다.')
            return False

        df.loc[index, columnName] = round(int(str(df.loc[index, columnName]).replace(',', '')), -(seatNum))
    
    return True

def roundUp(df:DataFrame, indexSize:int, columnName:str, seatNum:int) -> bool:
    if seatNum < 0:
        print('[Error] seatNum의 인자는 0를 초과해야합니다.')
        return False
    
    elif len(str(max(list(df.loc[:, columnName])))) < seatNum:
        print('[Error] 라운딩 업을 할 자리가 잘못 입력되었습니다.')
        return False

    for index in range(indexSize):
        if not str(df.loc[index, columnName]).replace(',', '').isdigit():
            print('[Error] 숫자형 데이터가 아닙니다.')
            return False

        data = list(map(int, str(df.loc[index, columnName]).replace(',', '')))

        if not data[-seatNum]:
            if set(data[-seatNum:]) == {0}:
                continue
        
        count = len(data[-seatNum:])
        data[-seatNum-1] += 1
        del data[-seatNum:]
        df.loc[index, columnName] = int(''.join(map(str, data)) + ('0' * count))

    return True

def roundDown(df:DataFrame, indexSize:int, columnName:str, seatNum:int) -> bool:
    if seatNum < 0:
        print('[Error] seatNum의 인자는 0를 초과해야합니다.')
        return False
    
    elif len(str(max(list(df.loc[:, columnName])))) < seatNum:
        print('[Error] 라운딩 다운을 할 자리가 잘못 입력되었습니다.')
        return False

    for index in range(indexSize):
        if not str(df.loc[index, columnName]).replace(',', '').isdigit():
            print('[Error] 숫자형 데이터가 아닙니다.')
            return False

        data = list(map(int, str(df.loc[index, columnName]).replace(',', '')))

        if not data[-seatNum]:
            if set(data[-seatNum:]) == {0}:
                continue
        
        count = len(data[-seatNum:])
        del data[-seatNum:]
        df.loc[index, columnName] = int(''.join(map(str, data)) + ('0' * count))

    return True

def controlRound(df:DataFrame, indexSize:int, columnName:str, originalAvg:int, originalSum:int, currentIndex:int, changeValue:int) -> bool:
    if len(df.loc[:, columnName]) <= currentIndex:
        print('[Error] 바꾸고자 하는 Index가 최대 Index보다 큽니다.')
        return False

    avg = numpy.mean(df.loc[:, columnName])
    sumData = sum(list(df.loc[:, columnName]))
    if originalAvg == avg:
        print('평균값이 원본과 같으므로 처리하지 않았습니다.')
        return True

    df.loc[currentIndex, columnName] = changeValue

    avg = numpy.mean(df.loc[:, columnName])
    sumData = sum(list(df.loc[:, columnName]))
    if originalAvg != avg:
        print(f'평균값이 원본과 같지 않습니다. 다시 입력해주세요. >>> {originalAvg} - {originalSum} : {avg} - {sumData}')
        return False

    return True

def standardized(df:DataFrame, indexSize:int, columnName:str):
    meanValue = numpy.mean(df.loc[:, columnName])
    stdValue = numpy.std(df.loc[:, columnName])

    for index in range(indexSize):
        print(df.loc[index, columnName], (df.loc[index, columnName] - meanValue) / stdValue)


if __name__ == '__main__':
    excel = pandas.read_excel('../test2.xlsx', index_col=0)
    excelSize = len(excel)
    
    # roundOff(excel, excelSize, '나이', 1)
    # roundUp(excel, excelSize, '회원번호', 2)
    # roundDown(excel, excelSize, '수입', 6)

    # avg = numpy.mean(df.loc[:, '나이'])
    # controlRound(excel, excelSize, '나이', avg, 8, 40)

    # print(sum(list(excel.loc[:, '나이'])) // excelSize)
    # print(excel)