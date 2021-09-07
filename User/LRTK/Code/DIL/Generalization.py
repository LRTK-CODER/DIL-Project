import pandas
from DIL import Error

DataFrame = pandas.DataFrame

class Generalization:
    def __init__(self, df:DataFrame):
        self.df = df

    def __errorControl(self, currentIndexList:list, column:str):
        try:
            if max(currentIndexList) > len(self.df):
                raise Error.Error('설정된 범위가 전체 크기보다 큽니다.')
            elif self.df.loc[:, column].dtype != 'int64':
                raise Error.Error('숫자형 데이터만 사용이 가능합니다.')
            
            return False
        except Exception as e:
            print('[Generaliztion Class Error]', e)
            return  True

    def local(self, column:str, currentIndexList:list) -> None:
        if self.__errorControl(currentIndexList, column):
            return
        
        datas = self.df.loc[currentIndexList[0]:currentIndexList[1], column]
        self.df.loc[currentIndexList[0]:currentIndexList[1], column] = [f'{min(datas)}~{max(datas)}' for _ in datas]

    def categorizion(self, column:str, replaceList:list, category:str) -> None:
        datas = self.df.loc[:, column]
        result = [category if data in replaceList else data for data in datas]
        self.df.loc[:, column] = result