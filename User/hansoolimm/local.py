import pandas

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

def run(datas:DataFrame, indexSize:int, columnName:str, scope:list) -> DataFrame:
    '''
    Creator : 임한수
    Data : 2021.07.17
    
    [Explanation]
    로컬 일반화를 위한 함수입니다.
    일반화할 범위를 설정하게 되며, 두 범위가 범위 대상이 0보다 작거나 허용 범위의 수보다 클 경우 에러가 호출됩니다.
    indexSize 값이 허용 범위 보다 클 시 에러가 호출됩니다
    일반화할 범위는 local(excel, indexSize, '대상 컬럼', [대상 범위])를 통해 변경할 수 있습니다.
    [Parameter]
    scope : 현재 특정범위를 임의로 설정하기 위해 범위를 인자값으로 저장
    '''
    
    dataList = list(datas.loc[scope[0]:scope[1], columnName])
    dataMin = min(dataList)
    dataMax = max(dataList)
    
    indexSize2 = len(datas)
    if indexSize > indexSize2:
        print("[Error] indexSize 가 허용범위를 넘었습니다.")
        return False

    if scope[0] < 0 :
        print("[Error] scope의 범위가 0보다 작습니다.")
        return False
    elif scope[1]+1 > indexSize2:
        print("[Error] scope의 범위가 최대 범위를 넘었습니다.")
        return False

    for index in range(scope[0], scope[1]+1):
        datas.loc[index, columnName] = f'{dataMin} ~ {dataMax}'
    
    return True

if __name__ == '__main__':
    excel = pandas.read_excel('../test2.xlsx', index_col=0)
    indexSize = len(excel)

    run(excel, indexSize, '수입', [1,3])
    print(excel)