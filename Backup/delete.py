import pandas

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

def partialSuppression(datas:DataFrame, indexSize:int, columnName:str, controlIndex:int, delMode:bool=True) -> DataFrame:
    #Error Control
    if controlIndex == 0:
            print('[Error] - Indexing 에러')
            return -1

    for index in range(indexSize):
            data = list(str(datas.loc[index, columnName]))
            
            if delMode:
                del data[:controlIndex]
            else:
                del data[controlIndex:]
            
            datas.loc[index, columnName] = ''.join(data)

    return datas

def RecordSupperesion(datas:DataFrame, currentIdexList:list) -> DataFrame:
    if len(datas) <= max(currentIdexList):
        print(f'최대 인덱스를 초과하였습니다. >>> {max(currentIdexList)}')
        return -1

    for idx in currentIdexList:
        datas = datas.drop([idx])
    
    return datas
    
def localSuppression(datas:DataFrame, columnName:str, currentIdexList:list) -> DataFrame:
    # Error Control
    if len(datas) < max(currentIdexList):
        print(f'[Error] - Data의 범위를 벗어났습니다. >>> {max(currentIdexList)}')
        return -1

    # Data Processing
    for index in currentIdexList:
        datas.loc[index, columnName] = ''

    return datas

if __name__ == '__main__':
    excel = pandas.read_excel('../test.xlsx', index_col=0)
    excelSize = len(excel)

    print(list(excel))

    # 부분 삭제
    print(excel.head())
    # print(partialSuppression(excel, excelSize, '전화번호', 5).head())
    # print(partialSuppression(excel, excelSize, '전화번호', 3, False).head())
    # print(partialSuppression(excel, excelSize, '전화번호', 0)) # Error
    # print(partialSuppression(excel, excelSize, '전화번호', 0, False).head()) # Error

    # 행 항목 삭제
    # print(RecordSupperesion(excel, [0, 2, 99]))
    # print(RecordSupperesion(excel, [0, 2, 100])) // Error

    # 로컬 삭제
    # print(localSuppression(excel, '회원번호', [1, 2, 3]).head())
    # Error Test
    localSuppression(excel, '회원번호', [1, 2, 101])