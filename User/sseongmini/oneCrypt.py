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