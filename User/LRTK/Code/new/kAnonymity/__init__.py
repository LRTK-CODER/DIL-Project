import pandas, time
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
        for index, row in self.df.iterrows():
            query = ' and '.join([f'({col} == "{row[col]}")' for col in self.columns])
            queryResult = self.df.query(query)
            # print(f'{index} 완료 >>>' + query)

            values.append(queryResult.shape[0])

        self.df.insert(0, 'k', values)

if __name__ == '__main__':
    excel = pandas.read_csv('../../../Sample/kTest_Full.csv', index_col=0)
    print('데이터 컬럼 >>>>', list(excel))

    test = Anonymity(excel, ['주소', '성별', '나이'])
    
    start = time.time()
    test.run()
    print("time :", time.time() - start)

    print(excel)
    # excel.to_csv('./result.csv', encoding='utf-8-sig') 
