import pandas
import hashlib

dataFrame = pandas.core.frame.DataFrame

# 단방향 암호화
# https://wikidocs.net/122201

class oneCrypt:
    
    m = hashlib.sha256()
    
    def oneEncrypt(self, dF:dataFrame, indexSize, columns):

        for i in range(indexSize):
            self.m.update(str(dF.loc[i, columns]).encode('utf-8'))
            dF.loc[i, columns] = self.m.hexdigest()

        return True

dataFrame = pandas.read_csv("C:/Users/zzxcv/Desktop/python/DIL/Sample/test_100.csv", index_col=0)
columns = '회원번호'
indexSize = dataFrame.shape[0]

a = oneCrypt()
a.oneEncrypt(dataFrame, indexSize, columns)
print(dataFrame['회원번호'])