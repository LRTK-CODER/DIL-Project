from typing import ClassVar
import pandas

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

def run(datas:DataFrame, indexSize:int, columnName:str, scope:list) -> DataFrame:
    '''
    Creator : 임한수
    Data : 2021.07.08
    
    [Explanation]
    마스킹 처리를 위한 함수입니다.
    두 입력 값을 받아 마스킹의 범위를 설정하게 되며 입력된 두 범위가 마스킹 대상의 크기보다 클 시 에러가 호출됩니다.
    마스킹할 범위는 masking(excel, excelSize, '회원번호'[x,y])를 통해 변경할 수 있습니다.
    이후 엑셀의 회원번호의 컬럼을 받아와 설정된 범위만큼 마스킹 처리합니다. 
    '''

    if len(scope) != 2:
       print('[Error] - 설정된 범위의 수가 잘 못 되었습니다.')
       return -1

    for index in range(indexSize):
        data = list(str(datas.loc[index, columnName]))
        for i in range(scope[0], scope[0]+1):
            data[i] = '*'
        
        datas.loc[index, columnName] = ''.join(data)
    print(datas)
    

if __name__ == '__main__':
    excel = pandas.read_csv('test2.csv', index_col=0)
    excelSize = len(excel)

    print(list(excel))
    run(excel, excelSize, '생일', [1, 2] )