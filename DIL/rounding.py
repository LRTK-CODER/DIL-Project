import pandas, random

DataFrame = pandas.DataFrame


class Rounding:
    @staticmethod
    def off(data: int, seatNum: int) -> int:
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
