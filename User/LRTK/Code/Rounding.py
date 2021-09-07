import pandas, error, random

DataFrame = pandas.DataFrame

class Rounding:
    def __errorControl(self, data:int, seatNum:int):
        try:
            if seatNum < 0:
                raise error.Error('라운딩할 자리는 0보다 커야합니다.')
            elif len(str(data)) < seatNum:
                raise error.Error('라운딩할 자리가 최대 범위를 넘어섰습니다.')

            return False
        except Exception as e:
            print('[SeatNum Error]', e)
            return  True

    def off(self, data:int, seatNum:int) -> int:
        if self.__errorControl(data, seatNum):
            return

        data = list(str(data))
        if int(data[-seatNum]) >= 5:
            data[-seatNum-1] = str(int(data[-seatNum-1]) + 1)
            data[-seatNum:] = '0' * len(data[-seatNum:])
        else:
            data[-seatNum:] = '0' * len(data[-seatNum:])
        
        return int(''.join(data))

    def up(self, data:int, seatNum:int) -> int:
        if self.__errorControl(data, seatNum):
            return

        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum-1] = str(int(data[-seatNum-1]) + 1)
            data[-seatNum:] = '0' * len(data[-seatNum:])

        return int(''.join(data))

    def down(self, data:int, seatNum:int) -> int:
        if self.__errorControl(data, seatNum):
            return

        data = list(str(data))
        if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
            data[-seatNum:] = '0' * len(data[-seatNum:])

        return int(''.join(data))

    def random(self, df:DataFrame, column:str) -> None:
        datas = df.loc[:, column]
        
        result = []
        for data in datas:
            func = random.choice([self.up, self.down])
            result.append(func(data=data, seatNum=len(str(data))-1))

        df.loc[:, column] = result
    
if __name__ == '__main__':
    excel = pandas.read_csv('../../../Sample/kTest_Full.csv', index_col=0)
    print(excel.head())
    
    round = Rounding()
    round.random(df=excel, column='총 구매 금액')
    print(excel.head())
