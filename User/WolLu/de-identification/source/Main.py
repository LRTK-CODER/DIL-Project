import pandas
from Output.DIL import Aggregation, Randomization
import Randomization
import KAnonymity
import LDiversity

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
    print('# 무작위화 #')
    print(' 6. 잡음추가 - 숫자형')
    print(' 7. 잡음추가 - 날짜형')
    print()
    print(' 0. 적용안함')
    print('======================')
    print()

# 알고리즘 선택 함수
def SelectAlgorithm(column: str, sel: int):
    noneMsg = '[!] 해당 알고리즘은 존재하지 않습니다.'

    if(sel == 0):
        return True
    elif(sel == 1):
        Aggregation.meanAggregation(dataFrame, indexSize, column, int(input("[+] 시작 인덱스 : ")), int(input("[+] 종료 인덱스 : ")), bool(input("[+] 반올림 : ")))
        return True
    elif (sel == 2):
        Aggregation.maxAggregation(dataFrame, indexSize, column, int(input("[+] 시작 인덱스 : ")), int(input("[+] 종료 인덱스 : ")))
        return True
    elif (sel == 3):
        Aggregation.minAggregation(dataFrame, indexSize, column, int(input("[+] 시작 인덱스 : ")), int(input("[+] 종료 인덱스 : ")))
        return True
    elif (sel == 4):
        Aggregation.midAggregation(dataFrame, indexSize, column, int(input("[+] 시작 인덱스 : ")), int(input("[+] 종료 인덱스 : ")))
        return True
    elif (sel == 5):
        Aggregation.modeAggregation(dataFrame, indexSize, column, int(input("[+] 시작 인덱스 : ")), int(input("[+] 종료 인덱스 : ")))
        return True
    elif (sel == 6):
        relatedColumns = []

        while(True):
            inputValue = input("[+] 연관된 퀄럼을 입력하세요(종료 : 0) : ")
            if inputValue == '0':
                break

            relatedColumns.append(inputValue)

        Randomization.noiseAdditionOfInt(dataFrame, indexSize, column, int(input("[+] 랜덤 최소값 : ")), int(input("[+] 랜덤 최대값 : ")), relatedColumns)
        return True
    elif (sel == 7):
        relatedColumns = []

        while (True):
            inputValue = input("[+] 연관된 퀄럼을 입력하세요(종료 : 0) : ")
            if inputValue == '0':
                break

            relatedColumns.append(inputValue)

        Randomization.noiseAdditionOfDate(dataFrame, indexSize, column, int(input("[+] 랜덤 최소값 : ")), int(input("[+] 랜덤 최대값 : ")), relatedColumns, input("[+] 날짜형식 %Y-%m-%d %H:%M:%S = 년도-월-일 시:분:초 : "))
        return True
    else:
        print(noneMsg)
        return False

# Entry Point
if __name__ == '__main__':
    url = input("[+] Enter Excel File Location : ")
    dataFrame = pandas.read_excel("../TestExcelFiles/test.xlsx", index_col=0)
    columns = list(dataFrame.columns)
    indexSize = dataFrame.shape[0]
    print('[*] 총 ', len(columns), '개의 퀄럼을 찾았습니다!', sep='')

    i = 1
    while (i < len(columns) + 1):
        PrintDidaAlgorithm()
        print("[+]", i, columns[i - 1], ': ', end='')

        if not (SelectAlgorithm(columns[i - 1], int(input()))):
            continue

        i += 1
        if not i < len(columns) + 1:
            print(columns)
            # K-익명성 검사 START
            exceptionColumns = []
            while (True):
                inputValue = input("[+] K-익명성 검사에서 제외할 퀄럼을 지정해주세요! [종료 : 0] : ")
                if inputValue == '0':
                    break

                exceptionColumns.append(inputValue)
            print(KAnonymity.kAnonymity(dataFrame, indexSize, exceptionColumns))
            # K-익명성 검사 END & L-다양성 검사
            print(LDiversity.lDiversity(dataFrame, input("[+] L-다양성 검사에서 사용할 동질집합 퀄럼을 지정해주세요! : "), input("[+] L-다양성 검사에서 사용할 퀄럼을 지정해주세요! : ")))

            inputValue = input("[+] 비식별화를 다시 진행할까요? [현재 데이터는 유지됩니다] : ")
            if inputValue != '0':
                i = 1

    print(dataFrame)
    dataFrame.to_excel("../TestExcelFiles/result.xlsx", sheet_name="Sheet1")