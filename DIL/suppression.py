from .util import DataSetting


class Suppression(DataSetting):
    """
    Creator : 오석재 & 임한수
    Data : 2021.09.01

    [Explanation]
        삭제 기술(일반 삭제, 부분 삭제, 행 항목 삭제, 마스킹)을 구현한 클래스
        모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다. 그래서 반환 값이 없음.
    """

    def __intCheck(self, datas):
        if datas.dtype == "int64":
            return True
        return False

    def general(self, columns: list = None) -> None:
        for col in columns:
            del self.datas[col]

        return True

    def partial(self, column: str, scope: list) -> None:
        datas = self.datas[column]

        # int형 타입 검사 및 str 변환
        intFlag = False
        if self.__intCheck(datas):
            datas = datas.astype("str")
            intFlag = True

        result = list()
        for data in datas:
            data = list(data)
            del data[scope[0] : scope[1] + 1]

            result.append("".join(data))

        if intFlag:
            result = list(map(int, result))

        self.datas[column] = result
        return self.datas[column]

    def record(self, currentIndexList: list) -> None:
        self.datas.drop(currentIndexList, axis=0, inplace=True)
        return self.datas

    def local(self, column: str, currentIndexList: list) -> None:
        datas = self._toList(column)

        for idx in currentIndexList:
            datas[idx] = ""

        self.datas[column] = datas

    def masking(self, column: str, scope: list) -> None:
        datas = self.datas[column]

        # int형 타입 검사 및 str 변환
        if self.__intCheck(datas):
            datas = datas.astype("str")

        result = list()
        for data in datas:
            data = list(data)
            data[scope[0] : scope[1]] = "*" * (scope[1] - scope[0])

            result.append("".join(data))

        self.datas[column] = result
        return self.datas[column]

    def address(self, column: str, mode: int = 2):
        if mode == 1:
            self.__stateRearDel(column)
        else:
            self.__cityRearDel(column)

        return self.datas[column]

    def __stateRearDel(self, column: str):
        datas = self._toList(column)

        result = [data.split()[0] for data in datas]
        self.datas[column] = result

    def __cityRearDel(self, column: str):
        datas = self._toList(column)

        result = [" ".join(data.split()[:2]) for data in datas]
        self.datas[column] = result
