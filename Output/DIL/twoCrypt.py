import pandas
from cryptography.fernet import Fernet # 대칭키 암호화

dataFrame = pandas.core.frame.DataFrame

class Twocrypt:
    
    key = Fernet.generate_key() # 키 생성
    f = Fernet(key)

    def twoEncrypt(self, dF:dataFrame, indexSize, columns):

        '''Two-way encryption)
        Creator : 홍성민
        Version : 1.0.0
        Support Type : str 

        [Explanation]
            column의 모든 값들을 암호화 한다.
            양방향 암호화를 위해서 키 값을 보관하고 파일에 저장하여 개인이 보관하도록 한다.

        [Parameter]
            <No Additions>
        '''
        
        print('해당 암호화의 키값은 {} 입니다, 키를 잃어버리지 않도록 잘 보관해주세요!\n'.format(self.key.decode()))

        # 키를 파일에 저장
        with open('D:/python_code/sseongmini/test.txt', 'w') as file:
            file.write(str(self.key.decode()))

        for i in range(indexSize):
            dF.loc[i, columns] = self.f.encrypt(str(dF.loc[i, columns]).encode()).decode()

        return True

    def twoDecrypt(self, dF:dataFrame, indexSize, columns):
        
        '''
        Title : 양방향 복호화 (Two-way Decryption)
        Creator : 홍성민
        Version : 1.0
        Support Type : str 

        [Explanation]
            column의 모든 값들을 복호화 한다.
            양방향 암호화에서 보관되었던 개인 키를 이용하여 복호화를 진행한다.

        [Parameter]
            <None>
        '''

        # 파일에서 키를 읽기
        file = open('C:/python_code/sseongmini/test.txt', 'r')
        print('키값은 {} 입니다.\n'.format(file.read()))

        originkey = file.read()
        newf = Fernet(originkey)

        print(newf)

        for i in range(indexSize):
            dF.loc[i, columns] = self.f.decrypt(str(dF.loc[i, columns]).encode()).decode()

        return True