import hashlib, random, string

class Hashing:
    def __init__(self, plainList):
        self.plainList = plainList
        
    def saltCreate(self):
        salt = ''
        for i in range(50):
            salt += str(random.choice(string.ascii_letters + string.digits))

        return salt

    def sha256(self, randomSalt=False):
        result, saltList = [], []
        for plain in self.plainList:
            if randomSalt:
                while True:
                    salt = self.saltCreate()

                    m = hashlib.sha256()
                    m.update((salt + plain).encode())

                    if m.hexdigest() not in result:
                        saltList.append(salt)
                        break
            
            else:
                m = hashlib.sha256()
                m.update(plain.encode())

                if m.hexdigest() in result:
                    print('hash 충돌 >>>', plain)

            result.append(m.hexdigest())
            

        
        return result, saltList