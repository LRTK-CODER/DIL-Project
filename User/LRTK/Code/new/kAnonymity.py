import pandas

DataFrame = pandas.DataFrame

def isType(data:DataFrame):
    for col in data.columns:
        if data.loc[:, col].dtype != object:
            data.loc[:,col] = data.loc[:, col].astype(str)

def run(data:DataFrame, k=10, delete=False):
    isType(data)

    values = []
    for _, row in data.iterrows():
        # query = ' and '.join([f'({col} == "{row[col]}")' for col in data.columns])
        query = ' and '.join([f'({col} == "{row[col]}")' for col in ['이름']])
        result = data.query(query)

        values.append(result.shape[0])

    data.insert(0, 'k', values)
    
    if delete:
        result = data.query(f'k > {k}')
        return result

if __name__ == '__main__':
    excel = pandas.read_csv('../../Sample/kTest.csv', index_col=0)
    
    result = run(excel, delete=True)
    print(excel.head())
    print(result.head())

    Test