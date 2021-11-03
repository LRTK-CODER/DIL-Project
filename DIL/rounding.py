import pandas, random

DataFrame = pandas.DataFrame


class Rounding:
    @staticmethod
    def off(data: int, seatNum: int) -> int:
        """
        라운딩 기술 중 반올림을 수행하는 메소드

        Parameters
        ----------
        data : int
            반올림을 수행할 숫자형 타입 데이터
        seatNum : int
            반올림을 수행할 숫자형 타입 데이터의 자리수 위치

        Returns
        -------
        int type data
            기술 적용 성공 시 True 리턴
        """
        data = list(str(data))
        if int(data[-seatNum]) >= 5:
            data[-seatNum - 1] = str(int(data[-seatNum - 1]) + 1)
            data[-seatNum:] = "0" * len(data[-seatNum:])
        else:
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))

    @staticmethod
    def up(data: int, seatNum: int) -> int:
        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum - 1] = str(int(data[-seatNum - 1]) + 1)
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))

    @staticmethod
    def down(data: int, seatNum: int) -> int:
        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum:] = "0" * len(data[-seatNum:])

        return int("".join(data))

    @staticmethod
    def random(df: DataFrame, column: str) -> None:
        datas = df.loc[:, column]

        result = []
        for data in datas:
            func = random.choice([Rounding.up, Rounding.down])
            result.append(func(data=data, seatNum=len(str(data)) - 1))

        df.loc[:, column] = result

        return df[column]
