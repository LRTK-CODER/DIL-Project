import pandas
import hashlib

dataFrame = pandas.core.frame.DataFrame

class oneCrypt:

    m = hashlib.sha256()

    def oneEncrypt(self, dF:dataFrame, indexSize, columns):

        '''
        Title : 일방향 암호화 - 암호학적 해시함수 (One-way encryption - Cryptographic hash function)
        Creator : 홍성민
        Version : 1.0
        Support Type : str 

        [Explanation]
            복호화가 불가능한 단방향 암호화로서 해시 함수를 말한다.
            참고 : https://wikidocs.net/122201
            
        [Parameter]
            <None>
        '''
        
        for i in range(indexSize):
            self.m.update(str(dF.loc[i, columns]).encode('utf-8'))
            dF.loc[i, columns] = self.m.hexdigest()

        return True