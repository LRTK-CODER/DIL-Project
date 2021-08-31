import pandas, error

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

class Suppression:
    def __init__(self, df:DataFrame, column:str):
        self.df = df
        self.column = column
        self.datas = df.loc[:, column]
    
    def __errorControl(self, scope=None, data=None, currentIndexList=None) -> bool:
        try:
            if (scope and data) and (max(scope) >= len(data)):
                raise error.Message('최대범위를 넘어섰습니다.')
            elif currentIndexList and max(currentIndexList) >= len(self.df):
                raise error.Message('최대범위를 넘어섰습니다.')

        except Exception as e:
            print('[Error]', e)
            return  True
        
        return False

    def general(self, columns:list=None) -> None:
        if not columns:
            del self.df[self.column]
        else:
            for col in columns:
                del self.df[col]

    def partial(self, scope:list) -> None:
        result = []
        isDigit = False
        for data in self.datas:
            if type(data) is int:
                data = str(data)
                isDigit = True
            
            if self.__errorControl(scope=scope, data=data):
                return

            data = list(data)
            del data[scope[0]:scope[1]+1]

            if isDigit:
                result.append(int(''.join(data)))
            else:
                result.append(''.join(data))
        
        self.df.loc[:, self.column] = result

    def record(self, currentIndexList:list) -> None or DataFrame:
        if self.__errorControl(currentIndexList=currentIndexList):
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
    excel = pandas.read_csv('../../Sample/kTest_Full.csv', index_col=0)
    print(excel.head())

    delete = Suppression(excel, '전화번호')
    # delete.general(['이름', '성별'])
    # delete.partial(scope=[3,8])
    excel = delete.record(currentIndexList=[0,3])
    print(excel.head())