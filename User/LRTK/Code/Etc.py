import pandas, error

DataFrame = pandas.DataFrame

class Etc:
    def __errorControl(self, datas:int, seatNum:int):
        try:
            if seatNum < 0:
                raise error.Error('수정해야합니다.')
            elif len(str(data)) < seatNum:
                raise error.Error('수정해야합니다.')

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

if __name__ == '__main__':
    excel = pandas.read_csv('../../../Sample/kTest_Full.csv', index_col=0)
    print(excel.head())
    
    print(Etc.sampling(excel, 10).head())

    identify, nonIdentify = Etc.anatomization(excel, '회원번호', ['이름', '성별', '나이', '생일', '전화번호', '주소'])
    print(identify.head())
    print(nonIdentify.head())