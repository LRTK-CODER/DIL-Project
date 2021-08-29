import pandas
from random import randint
from datetime import datetime, timedelta

dataFrame = pandas.core.frame.DataFrame

class Randomization:
    # 숫자형 잡음 추가
    def noiseAdditionOfInt(self, df: dataFrame, indexSize: int, columnName: str, startNum: int, endNum: int, relatedColumns: list):
        '''
        Creator: 정재윤
        Create Date: 2021.07.17
        Last Modified Date: 2021.07.17
        Version: 1.0
        Support Type: Int, Float

        [Explanation]
        이 함수는 columnName 이름의 행의 모든 데이터에 random값 (startNum 부터 endNum까지)을 추가하고 추가한 값을,
        연관된 reletedColumns의 모든 퀄럼의 같은 행 데이터에도 추가함

        [Parameter]
        startNum : Random 잡음의 최소값
        endNum : Random 잡음의 최대값
        relatedColumns : 연관된 퀄럼의 이름
        '''

        for i in range(indexSize):
            rand = randint(startNum, endNum)
            df.loc[i, columnName] += rand
            for j in relatedColumns:
                df.loc[i, j] += rand

        return True

    # 날짜형 잡음 추가
    def noiseAdditionOfDate(self, df: dataFrame, indexSize: int, columnName: str, startNum: int, endNum: int, relatedColumns: list, dateFormat: str):
        '''
        Creator: 정재윤
        Create Date: 2021.07.17
        Last Modified Date: 2021.07.17
        Version: 1.0
        Support Type: Date(str)

        [Explanation]
        이 함수는 columnName 이름의 행의 모든 데이터에 random값 (startNum 부터 endNum까지)을 추가하고 추가한 값을,
        연관된 reletedColumns의 모든 퀄럼의 같은 행 데이터에도 추가함

        [Parameter]
        startNum : Random 잡음의 최소값
        endNum : Random 잡음의 최대값
        relatedColumns : 연관된 퀄럼의 이름
        dateFormat : 날짜형식 %Y-%m-%d %H:%M:%S = 년도-월-일 시:분:초
        '''

        for i in range(indexSize):
            randTime = timedelta(days=randint(startNum, endNum))
            currentTime = datetime.strptime(df.loc[i, columnName], dateFormat)

            df.loc[i, columnName] = (currentTime + randTime).strftime(dateFormat.encode('unicode-escape').decode()).encode().decode('unicode-escape')

            for j in relatedColumns:
                relatedCurrentTime = datetime.strptime(df.loc[i, j], dateFormat)
                df.loc[i, j] = (relatedCurrentTime + randTime).strftime(dateFormat.encode('unicode-escape').decode()).encode().decode('unicode-escape')

        return True