import pandas

DataFrame = pandas.DataFrame

class DI:
    def __init__(self, df:DataFrame):
        self.df = df

    def columnsDelete(self, columns:list):
        self.df.drop(columns, axis=1)
    
    def masking(self, column:str):
        self.df[column] = [data[0]+'**' for data in list(self.df.loc[:, column])]
    
    def coding(self, column:str, machingTable:dict):
        self.df[column] = [machingTable[data] for data in list(self.df.loc[:, column])]

    def rounding(self, column:str):
        self.df[column] = [round(data, -1) for data in list(self.df.loc[:, column])]

    def address(self, column:str):
        self.df[column] = [data.split()[0] for data in list(self.df.loc[:, column])]
            
if __name__ == '__main__':
    excel = pandas.read_csv('../../Sample/test.csv', index_col=0)
    
    test = DI(excel)
    test.columnsDelete(['생일', '전화번호'])
    test.masking('이름')
    test.coding('성별', {'남성':'M', '여성':'F'})
    test.rounding('나이')
    test.address('주소')

    excel.to_csv('../../Sample/kTest_Full.csv', encoding='utf-8-sig') 