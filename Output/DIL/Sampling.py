def run(datas:DataFrame, indexSize:int, percent:int) -> DataFrame:
    '''
    Creator : 임한수
    Data : 2021. .
    
    [Explanation]
    
    [Parameter]
    
    '''
    datas = datas.loc[:,].sample(n=indexSize//percent)
    return datas

if __name__ == '__main__':
    excel = pandas.read_excel('../test.xlsx', index_col=0)
    indexSize = len(excel)
    print(excel)
    print(run(excel, indexSize, percent=10))