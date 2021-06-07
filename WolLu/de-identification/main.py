from DIDA import DIDA

# 알고리즘 목록 출력 함수
def PrintDidaAlgorithm():
    print()
    print('======================')
    print('# 가명처리 #')
    print(' 11. 휴리스틱 가명화')
    print('  0. 사람 이름')
    print('  1. 회사 이름')
    print(' 12. 암호화')
    print('  0. MD5 알고리즘')
    print('  1. SHA-256 알고리즘')
    print(' 13. 교환 방법')
    print()
    print('# 총계처리 #')
    print(' 21. 총계처리')
    print(' 22. 부분총계')
    print(' 23. 라운딩')
    print(' 24. 재배열')
    print()
    print('# 데이터 삭제 #')
    print(' 31. 식별자 삭제')
    print(' 32. 식별자 부분삭제')
    print(' 33. 레코드 삭제')
    print(' 34. 식별요소 전부삭제')
    print()
    print('# 데이터 범주화 #')
    print(' 41. 감추기')
    print(' 42. 랜덤 라운딩')
    print(' 43. 범위 방법')
    print(' 44. 제어 라운딩')
    print()
    print('# 데이터 마스킹 #')
    print(' 51. 임의 작음 추가')
    print(' 52. 공백과 대체')
    print()
    print(' 0. 적용안함')
    print('======================')
    print()

# 알고리즘 선택 함수
def SelectAlgorithm(column: str, sel: int):
    noneMsg = '해당 알고리즘은 존재하지 않습니다.'

    if(sel == 0):
        return True
    elif(sel == 11):
        return dida.HeuristicAlgorithm(column, rowsCount, int(input("모드 선택 : ")))
    elif(sel == 12):
        return dida.EncryptionAlgorithm(column, rowsCount, int(input("모드 선택 : ")))
    elif(sel == 13):
        print(noneMsg)
        return False
    elif(sel == 21):
        print(noneMsg)
        return False
    elif(sel == 22):
        print(noneMsg)
        return False
    elif(sel == 23):
        print(noneMsg)
        return False
    elif(sel == 24):
        print(noneMsg)
        return False
    elif(sel == 31):
        print(noneMsg)
        return False
    elif(sel == 32):
        print(noneMsg)
        return False
    elif(sel == 33):
        print(noneMsg)
        return False
    elif(sel == 34):
        print(noneMsg)
        return False
    elif(sel == 41):
        print(noneMsg)
        return False
    elif(sel == 42):
        print(noneMsg)
        return False
    elif(sel == 43):
        print(noneMsg)
        return False
    elif(sel == 44):
        print(noneMsg)
        return False
    elif(sel == 51):
        print(noneMsg)
        return False
    elif(sel == 52):
        print(noneMsg)
        return False
    else:
        print(noneMsg)
        return False

# Entry Point
if __name__ == '__main__':
    dida = DIDA('./test.xlsx')
    columns = dida.ReadColumnsToString()                           # 퀄럼 문자열(list)로 가져오기
    rowsCount = dida.GetDataFrameRowCount()                        # 행 개수 가져오기
    print('총 ', len(columns), '개의 퀄럼을 찾았습니다!', sep='')      # 행 개수 출력

    i = 1
    while(i < len(columns) + 1):
        PrintDidaAlgorithm()
        print(i, columns[i - 1], ': ', end='')

        if not (SelectAlgorithm(columns[i - 1], int(input()))):
            continue

        i += 1

    dida.print()                                                    # 최종 결과물을 콘솔에 출력
    dida.ExportExcelFile("result.xlsx")                             # 최종 결과물을 엑셀파일로 출력