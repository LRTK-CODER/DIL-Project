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

    def isType(self):
        for col in self.columns:
            if self.df.loc[:, col].dtype != object:
                self.df.loc[:, col] = self.df.loc[:, col].astype(str)

    def run(self):
        self.isType()

        values = []
        for _, row in self.df.iterrows():
            query = ' and '.join([f'({col} == "{row[col]}")' for col in self.df.columns])
            queryResult = self.df.query(query)

            values.append(queryResult.shape[0])

        self.df.insert(0, 'k', values)

if __name__ == '__main__':
    excel = pandas.read_csv('../../../Sample/kTest.csv', index_col=0)
    print('데이터 컬럼 >>>>', list(excel))

    test = Anonymity(excel, ['성별', '나이', '주소'])
    test.run()
    print(excel)
    # excel.to_csv('./result.csv', encoding='utf-8-sig') 
