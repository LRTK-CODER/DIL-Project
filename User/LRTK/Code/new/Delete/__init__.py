import pandas, error
from pandas.core.arrays import boolean

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

class Suppression:
    def __init__(self, df:DataFrame, column:str):
        self.df = df
        self.column = column
        self.datas = df.loc[:, column]
    
    def __errorControl(self) -> boolean:
        try:
            if len(str(data)) < seatNum:
                raise error.MaximumRangeError

        except Exception as e:
            print('[SeatNum Error]', e)
            return  False
        
        return True

    def partial(self, scope:list) -> None:
        result = []
        for data in self.datas:
            if type(data) is int:
                data = str(data)
            
            data = list(data)
            del data[scope[0]:scope[1]+1]
            result.append(''.join(data))
        
        self.df.loc[:, self.column] = result

    def record(self, currentIndexList:list) -> DataFrame:
        self.datas = self.df.values.tolist()
        
        for index in currentIndexList:
            del self.datas[index]
        
        return pandas

if __name__ == '__main__':
    excel = pandas.read_csv('../../../Sample/kTest_Full.csv', index_col=0)
    # print(excel.head())

    delete = Suppression(excel, '전화번호')
    # delete.partial(scope=[3,8])
    # delete.record(currentIndexList=[0,4])
    # print(excel.head())