import hashlib, random, string

class Hashing:
    def __init__(self, plainList, salt=None):
        self.plainList = plainList
        self.salt = salt

    def saltCreate(self):
        salt = ''
        for i in range(50):
            salt += str(random.choice(string.ascii_letters + string.digits))

        return salt

    def sha256(self, randomSalt=False):
        if not(self.salt):
            self.salt = saltCreate()

        result = []
        for plain in self.plainList:
            m = hashlib.sha256()
            m.update(self.salt + plain)
            result.append(m.hexdigest())
        
        return result