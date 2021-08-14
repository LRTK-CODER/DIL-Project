import pandas, time

DataFrame = pandas.DataFrame

def columnDelete(data:DataFrame, currentList:list):
    data.drop(currentList, axis=1, inplace=True)

def masking(data:DataFrame, column:str, start:int):
    for index in range(len(data)):
        data.loc[index, column] = data.loc[index, column][0] + ('*' * (len(data.loc[index, column])-start))

def coding(data:DataFrame, column:str, machingTable:dict):
    for index in range(len(data)):
        value = data.loc[index, column]
        
        if value in list(machingTable.keys()):
            data.loc[index, column] = machingTable[data.loc[index, column]]

def rounding(data:DataFrame, column:str):
    for index in range(len(data)):
        data.loc[index, column] = round(data.loc[index, column], -1)

def address(data:DataFrame, column:str):
    for index in range(len(data)):
        data.loc[index, column] = data.loc[index, column].split()[0]

if __name__ == '__main__':
    excel = pandas.read_csv('../../Sample/test_100.csv', index_col=0)
    
    start = time.time()
    columnDelete(excel, ['회원번호', '생일', '전화번호'])
    masking(excel, '이름', 1)
    coding(excel, '성별', {'남성':'m', '여성':'f'})
    rounding(excel, '나이')
    address(excel, '주소')
    print("time :", time.time() - start)

    print(excel.head())
    # ------------------------------------------------------
    data = excel.loc[:, ['이름', '성별', '나이', '주소']]
    data.to_csv('../../Sample/kTest.csv', encoding='utf-8-sig')