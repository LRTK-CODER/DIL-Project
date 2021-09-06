import pandas, error

# Data Type Definition
DataFrame = pandas.core.frame.DataFrame

class Suppression:
    """
        Creator : 오석재 & 임한수
        Data : 2021.09.01
        
        [Explanation]
            삭제 기술(일반 삭제, 부분 삭제, 행 항목 삭제, 마스킹)을 구현한 클래스
            모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다. 그래서 반환 값이 없음.
    """

    def __init__(self, df:DataFrame):
        self.df = df
        
    def __errorControl(self, columns:list=None, scope:list=None, data:str=None, currentIndexList:list=None) -> bool:
        try:
            if columns:
                for col in columns:
                    if col not in list(self.df):
                        raise error.Error('삭제하고자 하는 컬럼이 없습니다.')

            if (scope and data) and (max(scope) >= len(data)):
                raise error.Error('삭제하고자 하는 데이터의 최대범위를 넘어섰습니다.')

            if currentIndexList and max(currentIndexList) >= len(self.df):
                raise error.Error('최대범위를 넘어섰습니다.')
            

        except Exception as e:
            print('[Error]', e)
            return  True
        
        return False

    def general(self, columns:list=None) -> None:
        if self.__errorControl(columns=columns):
            return

        for col in columns:
            del self.df[col]

    def partial(self, column:str, scope:list) -> None:
        datas = self.df.loc[:, column]
        
        # int형 타입 검사 및 str 변환
        intCheck = False
        if datas.dtypes == 'int64':
            datas = datas.astype('str')
            intCheck = True

        result = list()
        for data in datas:
            # Error Control            
            if self.__errorControl(scope=scope, data=data):
                return

            data = list(data)
            del data[scope[0]:scope[1]+1]
            
            result.append(''.join(data))

        if intCheck:
           result = list(map(int, result))

        self.df.loc[:, column] = result

    def record(self, currentIndexList:list) -> None:
        if self.__errorControl(currentIndexList=currentIndexList):
            return

        self.df.drop(currentIndexList, axis=0, inplace=True)

    def local(self, column:str, currentIndexList:list) -> None:
        if self.__errorControl(currentIndexList=currentIndexList):
            return
        
        datas = list(self.df.loc[:, column])
        for idx in currentIndexList:
            datas[idx] = ''
        
        self.df.loc[:, column] = datas

    def masking(self, column:str, scope:list) -> None:
        datas = self.df.loc[:, column]
        
        # int형 타입 검사 및 str 변환
        if datas.dtypes == 'int64':
            datas = datas.astype('str')

        result = list()
        
        for data in datas:
            if self.__errorControl(scope=scope, data=data):
                return
            
            data = list(data)
            data[scope[0]:scope[1]] = '*' * (scope[1] - scope[0])

            result.append(''.join(data))

        self.df.loc[:, column] = result