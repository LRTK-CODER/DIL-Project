import pandas
import hashlib
from random import randrange

class DIDA:
    TYPE_ERROR_MSG = "해당 타입에 맞지 않는 알고리즘입니다."
    HEURISTIC_HUMAN_NAME = ['홍길동', '김민준', '정현우', '박준혁', '이영진', '오영식', '김예준']
    HEURISTIC_COMPANY_NAME = ['금성', '화성', '팔성', '대우']

    # 생성자
    def __init__(self, url: str):
        self.dataFrame = pandas.read_excel(url)

    # 휴리스틱 가명화 알고리즘 : Type('string'), Mode(0 : 이름, 1 : 회사명)
    def HeuristicAlgorithm(self, columnName: str, rowsCount: int, mode: int):
        # 사용 가능한 타입 검사
        if not type(self.dataFrame.loc[0, columnName]) == type("string"):
            print(self.TYPE_ERROR_MSG)
            return False

        # 실제 로직
        if mode == 0:                                       # 모드 0 : 사람이름
            for i in range(rowsCount):
                self.dataFrame.loc[i, columnName] = self.HEURISTIC_HUMAN_NAME[randrange(0, len(self.HEURISTIC_HUMAN_NAME))]

        if mode == 1:                                       # 모드 1 : 회사이름
            for i in range(rowsCount):
                self.dataFrame.loc[i, columnName] = self.HEURISTIC_COMPANY_NAME[0, len(self.HEURISTIC_COMPANY_NAME)]

        return True

    # 암호화 알고리즘 : Type('ALL'), Mode(0 : MD5, 1 : SHA356)
    def EncryptionAlgorithm(self, columnName: str, rowsCount: int, mode: int):
        if mode == 1:
            hash = hashlib.sha256()
        else:
            hash = hashlib.md5()

        for i in range(rowsCount):
            hash.update(str(self.dataFrame.loc[i, columnName]).encode('utf-8'))
            self.dataFrame.loc[i, columnName] = hash.hexdigest()

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