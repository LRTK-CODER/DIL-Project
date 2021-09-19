import pandas, Error

DataFrame = pandas.DataFrame

class Etc:
    def __errorControl(self, datas:int, seatNum:int):
        try:
            if seatNum < 0:
                raise Error.Error('수정해야합니다.')
            elif len(str(data)) < seatNum:
                raise Error.Error('수정해야합니다.')

            return False
        except Exception as e:
            print('[SeatNum Error]', e)
            return  True

    def sampling(self, datas:DataFrame, percent:int) -> DataFrame:
        datas = datas.loc[:,].sample(n=len(datas)//percent)
        return datas

    def anatomization(self, datas:DataFrame, codeColumn:str, currentColumnList:list) -> DataFrame:
        currentColumnList.insert(0, codeColumn)
        nonCurrentColumnList = list(set(list(datas)) - set(currentColumnList))
        nonCurrentColumnList.insert(0, codeColumn)
        
        return datas.loc[:, currentColumnList], datas.loc[:, nonCurrentColumnList]