import pandas as pd, random
from korean_name_generator import namer

class DataCreate:
    def __init__(self, memberNumber=10000, dataCount=100):
        self.memberNumber = memberNumber
        self.dataCount = dataCount

    def memberNumberCreate(self):
        return [self.memberNumber + i for i in range(1, self.dataCount+1)]

    def nameCreate(self, maleRatio=0.7, femaleRatio=0.3):
        maleName = [namer.generate(True) for _ in range(int(self.dataCount * maleRatio))]
        femaleName = [namer.generate(False) for _ in range(int(self.dataCount * femaleRatio))]
        return maleName + femaleName

    def genderList(self, maleRatio=0.7, femaleRatio=0.3):
        male = ['male' for _ in range(int(self.dataCount * maleRatio))]
        female = ['female' for _ in range(int(self.dataCount * femaleRatio))]
        return male + female

    def phoneNumberCreate(self):
        result = []
        for _ in range(self.dataCount):
            mid = str(random.randrange(1, 9999))
            if len(mid) < 4:
                mid = ('0' * (4-len(mid))) + mid

            bottom = str(random.randrange(1, 9999))
            if len(bottom) < 4:
                bottom = ('0' * (4-len(bottom))) + bottom

            result.append(f'010-{mid}-{bottom}')

        return result

    def ageCreate(self, start, end):
        return [random.randrange(start, end) for _ in range(self.dataCount)]

    def birthCreate(self):
        result = []
        for _ in range(self.dataCount):
            month = random.randrange(1, 12)
            day = random.randrange(1, 31)

            if month == 2:
                if day > 28:
                    day = 28

            result.append(f'{month}월 {day}일')

        return result

if __name__ == '__main__':
    data = DataCreate()

    memberNumber = data.memberNumberCreate()
    nameList = data.nameCreate()
    genderList = data.genderList()
    age = data.ageCreate(20, 80)
    birth = data.birthCreate()
    phoneNumber = data.phoneNumberCreate()

    datas = {
        '회원번호': memberNumber,
        '이름': nameList,
        '성별': genderList,
        '나이': age,
        '생일': birth,
        '전화번호': phoneNumber
    }
    df = pd.DataFrame(datas)

    df.to_excel('test.xlsx')
