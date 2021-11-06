import pandas, random

DataFrame = pandas.DataFrame


class Rounding:
    """
    라운딩 기술(일반 라운딩, 랜덤 라운딩)을 구현한 클래스
    """

    @staticmethod
    def off(data: int, seatNum: int):
        """
        라운딩 기술 중 반올림을 수행하는 메소드

        Parameters
        ----------
            - data : int
                반올림을 수행할 숫자형 타입 데이터
            - seatNum : int
                반올림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns
        -------
            - int type data
                반올림이 적용된 숫자형 타입 데이터를 리턴
        """
        data = list(str(data))
        if int(data[-seatNum]) >= 5:
            data[-seatNum - 1] = str(int(data[-seatNum - 1]) + 1)
            data[-seatNum:] = "0" * len(data[-seatNum:])
        else:
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))

    @staticmethod
    def up(data: int, seatNum: int):
        """
        라운딩 기술 중 올림을 수행하는 메소드

        Parameters
        ----------
            - data : int
                올림을 수행할 숫자형 타입 데이터
            - seatNum : int
                올림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns
        -------
            - int type data
                올림이 적용된 숫자형 타입 데이터를 리턴
        """
        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum - 1] = str(int(data[-seatNum - 1]) + 1)
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))

    @staticmethod
    def down(data: int, seatNum: int):
        """
        라운딩 기술 중 내림을 수행하는 메소드

        Parameters
        ----------
            - data : int
                내림을 수행할 숫자형 타입 데이터
            - seatNum : int
                내림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns
        -------
            - int type data
                내림이 적용된 숫자형 타입 데이터를 리턴
        """
        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))

    @staticmethod
    def random(df: DataFrame, column: str):
        """
        라운딩 기술 중 무작위로 수행하는 메소드

        Parameters
        ----------
            - data : int
                무작위로 수행할 숫자형 타입 데이터
            - seatNum : int
                무작위로 수행할 숫자형 타입 데이터의 자리수 위치

        Returns
        -------
            - True
                기술 적용 성공 시 True 리턴
        """
        datas = df.loc[:, column]

        result = []
        for data in datas:
            func = random.choice([Rounding.up, Rounding.down])
            result.append(func(data=data, seatNum=len(str(data)) - 1))

        df.loc[:, column] = result

        return True
