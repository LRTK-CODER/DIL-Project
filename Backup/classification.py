import pandas

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

def run(datas:DataFrame, indexSize:int, columnName:str, replaceValue:str) -> DataFrame:
    '''
    Creator : 임한수
    Data : 2021.07.17
    
    [Explanation]
    문자데이터 범주화 처리를 위한 함수입니다.
    특정 컬럼 값을 받아 범주화 범위를 설정하게 되며, indexSize 값이 허용 범위 보다 클 시 에러가 호출됩니다.
    classification(excel, indexSize, '특정컬럼 이름', '변경할 문자데이터')를 통해 변경할 수 있습니다.
    [Parameter]
    replaceValue : 변경할 문자데이터 인자값을 저장

    
    '''
    indexSize2 = len(datas)
    if indexSize > indexSize2:
        print("indexSize 가 허용범위를 넘었습니다.")
        return False

    for index in range(indexSize):
        datas.loc[index, columnName] = replaceValue
        
    return True
 
if __name__ == '__main__':
    excel = pandas.read_excel('../test2.xlsx', index_col=0)
    indexSize = len(excel)

    run(excel, indexSize, '기관명', '회사')
    print(excel)

    