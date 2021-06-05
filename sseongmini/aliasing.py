from cryptography.fernet import Fernet
import pandas as pd, random
import numpy as np

# 암호화
class SimpleEnDecrypt:
    def __init__(self, key=None):
        if key is None: # 키가 없다면
            key = Fernet.generate_key() # 키를 생성한다
        self.key = key
        self.f   = Fernet(self.key)
    
    def encrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.encrypt(data) # 바이트형태이면 바로 암호화
        else:
            ou = self.f.encrypt(data.encode('utf-8')) # 인코딩 후 암호화
        if is_out_string is True:
            return ou.decode('utf-8') # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou
        
    def decrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.decrypt(data) # 바이트형태이면 바로 복호화
        else:
            ou = self.f.decrypt(data.encode('utf-8')) # 인코딩 후 복호화
        if is_out_string is True:
            return ou.decode('utf-8') # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou

simpleEnDecrypt = SimpleEnDecrypt()

df = pd.read_excel('test.xlsx')

name_list = ["홍길동", "임꺽정", "김철수", "이영희"]

# 무작위로 가명을 선택한 후 암호화하여 저장
for i in range(len(df['이름'])):
    encrypt_text = simpleEnDecrypt.encrypt(np.random.choice(list(name_list)))
    print(encrypt_text)

print(df['이름'])

# 암호화 코드 출처 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221666489901