import pandas, error

DataFrame = pandas.DataFrame

def Sampling(datas:DataFrame, indexSize:int, percent:int) -> DataFrame:
    datas = datas.loc[:,].sample(n=indexSize//percent)
    return datas

if __name__ == '__main__':
    excel = pandas.read_excel('../../../Sample/kTest_Full.csv', index_col=0)
    indexSize = len(excel)
    print(excel)
    print(run(excel, indexSize, percent=10))