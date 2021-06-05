import base64
import hashlib

from Cryptodome import Random
from Cryptodome.Cipher import AES

class MyCipher:
 def __init__(self):
     self.BS = 16
     self.pad = lambda s: s + (self.BS-len(s.encode('utf-8'))%self.BS)*chr(self.BS-len(s.encode('utf-8'))%self.BS)
     self.unpad = lambda s:s[0:-s[-1]]
     self.key = hashlib.sha256().digest()


 def encrypt(self,raw):
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key.AES.MODE_CFB, iv)
        return base64.b64encode(iv+cipher.encrypt(raw.encode('utf-8')))

 def decrypt(self,enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key.AES.MODE_CFB, iv)
        return self.unpad(cipher.decrypt(enc[16:]))

 def encrypt_str(self,raw):
        return self.encrypt(raw).decode('utf-8')

 def decrypt_str(self,enc):
        if type(enc)==str:
         enc = str.encode(enc)
        return self.decrypt(enc).decode('utf-8')
     
