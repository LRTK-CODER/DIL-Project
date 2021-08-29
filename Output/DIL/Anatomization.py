import pandas, numpy, copy

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

def Anatomization(df:DataFrame, indexSize:int, currentList:list) -> DataFrame:
    dfCopy = copy.deepcopy(df)
    columnList = list(dfCopy)

    trueColumnList = list(set(columnList) - set(currentList))
    return dfCopy[trueColumnList], dfCopy[currentList]

if __name__ == '__main__':
    excel = pandas.read_excel('../test.xlsx', index_col=0)
    excelSize = len(excel)
    
    print(excel)
    dfTrue, dfFalse = anatomization(excel, excelSize, currentList=['성별', '나이'])
    print(dfTrue)

