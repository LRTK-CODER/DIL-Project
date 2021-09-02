import pandas
from cryptography.fernet import Fernet # 대칭키 암호화

dataFrame = pandas.core.frame.DataFrame

class twoCrypt:
    
    originkey = ''

    # 양방향 암호화
    def twoEncrypt(self, dF:dataFrame, indexSize, columns):
        
        self.key = Fernet.generate_key() # 키 생성
    
        print('해당 암호화의 키값은 {} 입니다, 키를 잃어버리지 않도록 잘 보관해주세요!\n'.format(self.key.decode()))

        f = Fernet(self.key)
        # 키를 파일에 저장
        with open('test.txt', 'w') as file:
            file.write(str(self.key.decode()))

        for i in range(indexSize):
            dF.loc[i, columns] = f.encrypt(str(dF.loc[i, columns]).encode()).decode()

        return True

    def twoDecrypt(self, dF:dataFrame, indexSize, columns):

        # 파일에서 키를 읽기
        file = open('test.txt', 'r')
        originkey = file.readline()
        print('키값은 {} 입니다.\n'.format(originkey))
        f = Fernet(originkey.encode())

        for i in range(indexSize):
            dF.loc[i, columns] = f.decrypt(str(dF.loc[i, columns]).encode()).decode()

        return True


dataFrame = pandas.read_csv("../../Sample/test_100.csv", index_col=0)
columns = '회원번호'
indexSize = dataFrame.shape[0]

a = twoCrypt()
a.twoEncrypt(dataFrame, indexSize, columns)
a.twoDecrypt(dataFrame, indexSize, columns)
print(dataFrame['회원번호'])