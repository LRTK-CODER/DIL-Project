import pandas
import hashlib

dataFrame = pandas.core.frame.DataFrame

# 단방향 암호화
# https://wikidocs.net/122201
m = hashlib.sha256()

def oneEncrypt(dF:dataFrame, indexSize, columns):

    for i in range(indexSize):
        m.update(str(dF.loc[i, columns]).encode('utf-8'))
        dF.loc[i, columns] = m.hexdigest()

    return True

if __name__ == '__main__':
    dataFrame = pandas.read_excel('D:/python_code/sseongmini/test.xlsx', index_col=0)
    columns = list(dataFrame.columns)
    indexSize = dataFrame.shape[0]

    oneEncrypt(dataFrame, indexSize, '성별')
    print(dataFrame)