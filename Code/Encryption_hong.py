import pandas
from cryptography.fernet import Fernet # 대칭키 암호화

dataFrame = pandas.core.frame.DataFrame

key = Fernet.generate_key() # 키 생성

f = Fernet(key)

# 양방향 암호화
def twoEncrypt(dF:dataFrame, indexSize, columns):
    
    print('해당 암호화의 키값은 {} 입니다, 키를 잃어버리지 않도록 잘 보관해주세요!\n'.format(key.decode()))

    # 키를 파일에 저장
    with open('D:/python_code/sseongmini/test.txt', 'w') as file:
        file.write(str(key.decode()))

    for i in range(indexSize):
        dF.loc[i, columns] = f.encrypt(str(dF.loc[i, columns]).encode()).decode()

    return True

def twoDecrypt(dF:dataFrame, indexSize, columns):

    # 파일에서 키를 읽기
    file = open('D:/python_code/sseongmini/test.txt', 'r')
    print('키값은 {} 입니다.\n'.format(file.read()))

    originkey = file.read()
    # f = Fernet(originkey)

    for i in range(indexSize):
        dF.loc[i, columns] = f.decrypt(str(dF.loc[i, columns]).encode()).decode()

    return True

if __name__ == '__main__':
    dataFrame = pandas.read_excel('D:/python_code/sseongmini/test.xlsx', index_col=0)
    columns = list(dataFrame.columns)
    indexSize = dataFrame.shape[0]

    twoEncrypt(dataFrame, indexSize, '회원번호')
    twoDecrypt(dataFrame, indexSize, '회원번호')

    print(dataFrame)