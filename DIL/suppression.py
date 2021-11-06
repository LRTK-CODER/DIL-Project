from .util import DataSetting


class Suppression(DataSetting):
    """
    | 삭제 기술(일반 삭제, 부분 삭제, 행 항목 삭제, 마스킹)을 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.

    Parameters
    ----------
        - datas : pandas.DataFrame
            삭제 기술을 적용할 DataFrame 지정
    """

    def __intCheck(self, datas):
        """
        기술 적용하고자 하는 DataFrame이 'int64 타입'으로 되어있는지 확인하는 함수

        Parameters
        ----------
            - datas : pandas.DataFrame
                int64 타입 검사를 진행할 DataFrame

        Returns
        -------
            - True or False
                | int64 타입이면 True 리턴
                | int64 타입이 아니면 False 리턴
        """
        if datas.dtype == "int64":
            return True
        return False

    def general(self, columns: list = None):
        """
        삭제 기술 중 일반 삭제를 수행하는 함수

        Parameters
        ----------
            - columns : list
                일반 삭제를 적용할 컬럼들

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
        for col in columns:
            del self.datas[col]

        return True

    def partial(self, column: str, scope: list):
        """
        삭제 기술 중 부분 삭제를 수행하는 함수

        Parameters
        ----------
            - column : str
                부분 삭제를 적용할 컬럼
            - scope : list
                데이터의 부분 삭제 적용 범위 지정

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
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

        return True

    def record(self, currentIndexList: list):
        """
        삭제 기술 중 행 항목 삭제를 수행하는 함수

        Parameters
        ----------
            - currentIndexList : list
                삭제 할 Index list

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
        self.datas.drop(currentIndexList, axis=0, inplace=True)

        return True

    def local(self, column: str, currentIndexList: list):
        """
        삭제 기술 중 로컬 삭제를 수행하는 함수

        Parameters
        ----------
            - column : str
                로컬 삭제 기술을 적용할 컬럼
            - currentIndexList : list
                로컬 삭제 기술을 적용할 Index list

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
        datas = self._toList(column)

        for idx in currentIndexList:
            datas[idx] = ""

        self.datas[column] = datas

        return True

    def masking(self, column: str, scope: list):
        """
        삭제 기술 중 마스킹을 수행하는 함수

        Parameters
        ----------
            - column : str
                마스킹 기술을 적용할 컬럼
            - scope : list
                데이터에 마스킹 기술을 적용할 범위 지정

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
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

        return True

    def address(self, column: str, mode: int = 2):
        """
        주소 부분 삭제를 수행하는 함수

        Parameters
        ----------
            - column : str
                주소 부분 삭제를 적용할 컬럼
            - mode: int
                | 값이 1일 때, 도 단위까지 부분 삭제
                | 값이 2일 때, 시 단위까지 부분 삭제
                | Default = 2

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
        if mode == 1:
            self.__stateRearDel(column)
        else:
            self.__cityRearDel(column)

        return True

    def __stateRearDel(self, column: str):
        datas = self._toList(column)

        result = [data.split()[0] for data in datas]
        self.datas[column] = result

    def __cityRearDel(self, column: str):
        datas = self._toList(column)

        result = [" ".join(data.split()[:2]) for data in datas]
        self.datas[column] = result
