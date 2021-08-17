import pandas
import error

DataFrame = pandas.DataFrame

class Anonymity:
    def __init__(self, df:DataFrame, columns:list, k:int=10):
        try:
            if columns == []:
                raise error.ColumnsEmptyError
            else:
                self.columns = columns
        except Exception as e:
            return print('[Init Error]', e)

        try:
            if k < 1:
                raise error.KSizeError
            else:
                self.k = k
        except Exception as e:
            return print('[Init Error]', e)

        self.df = df
        self.result, self.overlaps = {}, {}
        for col in self.columns:
            self.result[col] = {}
            self.overlaps[col] = sorted(list(set(self.df.loc[:, col])))

    def isType(self):
        for col in self.columns:
            if self.df.loc[:, col].dtype != object:
                self.df.loc[:, col] = self.df.loc[:, col].astype(str)

    def run(self):
        self.isType()

        for col in self.columns:
            for overlap in self.overlaps[col]:
                self.result[col][overlap] = len(self.df.query(f'{col} == "{overlap}"'))
        
        return self.result

if __name__ == '__main__':
    excel = pandas.read_csv('../../Sample/kTest.csv', index_col=0)
    print('데이터 컬럼 >>>>', list(excel))

    test = Anonymity(excel, ['이름', '성별', '나이', '주소'])
    print(test.run())
