import pandas, error
from pandas.core.arrays import boolean

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

class Suppression:
    def __init__(self, df:DataFrame, column:str):
        self.df = df
        self.column = column
        self.datas = df.loc[:, column]
    
    def __errorControl(self, scope=None, data=None, currentIndexList=None) -> boolean:
        try:
            if (scope and data) and (max(scope) >= len(data)):
                raise error.MaximumRangeError
            if currentIndexList and max(currentIndexList) >= len(self.df):
                raise error.MaximumRangeError

        except Exception as e:
            print('[Scope Error]', e)
            return  False
        
        return True

    def general(self):
        pass

    def partial(self, scope:list) -> None:
        result = []
        for data in self.datas:
            if type(data) is int:
                data = str(data)
            
            if not self.__errorControl(scope=scope, data=data):
                return

            data = list(data)

            del data[scope[0]:scope[1]+1]
            result.append(''.join(data))
        
        self.df.loc[:, self.column] = result

    def record(self, currentIndexList:list) -> None or DataFrame:
        if not self.__errorControl(currentIndexList=currentIndexList):
            return
        
        self.datas = self.df.values.tolist()
        
        for index in currentIndexList:
            del self.datas[index]
        
        return pandas.DataFrame(self.datas, columns=list(self.df))

    def local(self, currentIndexList:list):
        if not self.__errorControl(currentIndexList=currentIndexList):
            return

        result = []
        for data in self.datas:
            pass

    def masking(self):
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
    excel = pandas.read_csv('../../../Sample/kTest_Full.csv', index_col=0)
    print(excel.head())

    delete = Suppression(excel, '전화번호')
    # delete.partial(scope=[3,8])
    excel = delete.record(currentIndexList=[0,10000000000000])
    print(excel.head())