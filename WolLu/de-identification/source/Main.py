import pandas
import Aggregation

# 알고리즘 목록 출력 함수
def PrintDidaAlgorithm():
    print()
    print('======================')
    print('# 총계처리 #')
    print(' 1. 총계처리 - 평균값')
    print(' 2. 총계처리 - 최대값')
    print(' 3. 총계처리 - 최소값')
    print(' 4. 총계처리 - 중앙값')
    print(' 5. 총계처리 - 최빈값')
    print()
    print(' 0. 적용안함')
    print('======================')
    print()

# 알고리즘 선택 함수
def SelectAlgorithm(column: str, sel: int):
    noneMsg = '해당 알고리즘은 존재하지 않습니다.'

    if(sel == 0):
        return True
    elif(sel == 1):
        Aggregation.meanAggregation(dataFrame, indexSize, column, bool(input("반올림 : ")))
        return True
    elif (sel == 2):
        Aggregation.maxAggregation(dataFrame, indexSize, column)
        return True
    elif (sel == 3):
        Aggregation.minAggregation(dataFrame, indexSize, column)
        return True
    elif (sel == 4):
        Aggregation.midAggregation(dataFrame, indexSize, column)
        return True
    elif (sel == 5):
        Aggregation.modeAggregation(dataFrame, indexSize, column)
        return True
    elif (sel == 10):
        Aggregation.microAggregation(dataFrame, indexSize, column)
        return True
    else:
        print(noneMsg)
        return False

# Entry Point
if __name__ == '__main__':
    url = input("Enter Excel File Location : ")
    dataFrame = pandas.read_excel("../TestExcelFiles/test.xlsx")
    columns = list(dataFrame.columns)
    indexSize = dataFrame.shape[0]
    print('총 ', len(columns), '개의 퀄럼을 찾았습니다!', sep='')

    i = 1
    while (i < len(columns) + 1):
        PrintDidaAlgorithm()
        print(i, columns[i - 1], ': ', end='')

        if not (SelectAlgorithm(columns[i - 1], int(input()))):
            continue

        i += 1

    print(dataFrame)
    dataFrame.to_excel("../TestExcelFiles/result.xlsx", sheet_name="Sheet1")