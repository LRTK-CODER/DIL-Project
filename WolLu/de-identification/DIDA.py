import numpy
import pandas
import hashlib
import random

class DIDA:
    TYPE_ERROR_MSG = "해당 타입에 맞지 않는 알고리즘입니다."
    HEURISTIC_HUMAN_NAME = ['홍길동', '김민준', '정현우', '박준혁', '이영진', '오영식', '김예준']
    HEURISTIC_COMPANY_NAME = ['금성', '화성', '팔성', '대우']

    # 생성자
    def __init__(self, url: str):
        self.dataFrame = pandas.read_excel(url)

    # 휴리스틱 가명화 알고리즘 : Type('string'), Mode(0 : 이름, 1 : 회사명)
    def Heuristic(self, columnName: str, rowsCount: int, mode: int):
        # 사용 가능한 타입 검사
        if not str(type(self.dataFrame.loc[0, columnName])) == "<class 'str'>":
            print(self.TYPE_ERROR_MSG, type(self.dataFrame.loc[0, columnName]))
            return False

        # 실제 로직
        if mode == 0:                                       # 모드 0 : 사람이름
            for i in range(rowsCount):
                self.dataFrame.loc[i, columnName] = self.HEURISTIC_HUMAN_NAME[random.randrange(0, len(self.HEURISTIC_HUMAN_NAME))]

        if mode == 1:                                       # 모드 1 : 회사이름
            for i in range(rowsCount):
                self.dataFrame.loc[i, columnName] = self.HEURISTIC_COMPANY_NAME[0, len(self.HEURISTIC_COMPANY_NAME)]

        return True

    # 암호화 알고리즘 : Type('ALL'), Mode(0 : MD5, 1 : SHA356)
    def Encryption(self, columnName: str, rowsCount: int, mode: int):
        if mode == 1:
            hash = hashlib.sha256()
        else:
            hash = hashlib.md5()

        for i in range(rowsCount):
            hash.update(str(self.dataFrame.loc[i, columnName]).encode('utf-8'))
            self.dataFrame.loc[i, columnName] = hash.hexdigest()

        return True

    # 총계처리 알고리즘 : Type('int', 'float'), Mode(0 : 실수, 1 : 정수(사사오입 원칙에 따라 반올림))
    def Aggregation(self, columnName: str, rowsCount: int, start: float, end: float, mode: int):
        result: float = 0;

        # 사용 가능한 타입 검사
        if not str(type(self.dataFrame.loc[0, columnName])) == "<class 'numpy.int64'>" or str(type(self.dataFrame.loc[0, columnName])) == "<class 'numpy.float'>":
            print(self.TYPE_ERROR_MSG, type(self.dataFrame.loc[0, columnName]), type(numpy.int64))
            return False

        # 실제로직 & 전체총계
        if(start == 0 and end == 0):
            for i in range(rowsCount):
                result += self.dataFrame.loc[i, columnName]

            result /= rowsCount
            if(mode == 1):
                result = round(result)

            for i in range(rowsCount):
                self.dataFrame.loc[i, columnName] = '약 ' + str(result)

        # 부분총계
        else:
            count = 0

            for i in range(rowsCount):
                tmp = self.dataFrame.loc[i, columnName]
                if(tmp >= start and tmp <= end):
                    result += tmp
                    count += 1

            result /= count
            if (mode == 1):
                result = round(result)

            for i in range(rowsCount):
                tmp = self.dataFrame.loc[i, columnName]
                if (tmp >= start and tmp <= end):
                    self.dataFrame.loc[i, columnName] = '약' + str(result)

        return True

    # 라운딩 알고리즘 : Type('int', 'float'), Mode(0 : 나이, 1 : 그 외), Unit(단위 ex'천만'), SplitCount(뒤에서 부터 자를 자릿수)
    def Rounding(self, columnName: str, rowsCount: int, mode: int, unit: str, splitCount: int):
        # 사용 가능한 타입 검사
        if not str(type(self.dataFrame.loc[0, columnName])) == "<class 'numpy.int64'>" or str(
                type(self.dataFrame.loc[0, columnName])) == "<class 'numpy.float'>":
            print(self.TYPE_ERROR_MSG, type(self.dataFrame.loc[0, columnName]), type(numpy.int64))
            return False

        # 실제로직
        for i in range(rowsCount):
            if mode == 0:
                if self.dataFrame.loc[i, columnName] < 10:
                    self.dataFrame.loc[i, columnName] = "10대 미만"
                else:
                    self.dataFrame.loc[i, columnName] = str(self.dataFrame.loc[i, columnName])[:-1] + '0대'
            else:
                self.dataFrame.loc[i, columnName] = '약 ' + str(round(self.dataFrame.loc[i, columnName]))[:-splitCount] + unit

        return True

    # 재배열 알고리즘
    def Rearrangement(self, columnName: str, rowsCount: int):
        tmpList = []

        for i in range(rowsCount):
            tmpList.append(self.dataFrame.loc[i, columnName])

        random.shuffle(tmpList)

        for i in range(rowsCount):
            self.dataFrame.loc[i, columnName] = tmpList[i]

        return True

    # 퀄럼 문자열 출력 메서드
    def ReadColumnsToString(self):
        return list(self.dataFrame.columns)

    # DataFrame 행 개수 반환 메서드
    def GetDataFrameRowCount(self):
        return self.dataFrame.shape[0]

    # DataFrame 엑셀 파일로 출력
    def ExportExcelFile(self, fileName: str):
        self.dataFrame.to_excel(fileName, sheet_name = "Sheet1")

    def print(self):
        print(self.dataFrame)