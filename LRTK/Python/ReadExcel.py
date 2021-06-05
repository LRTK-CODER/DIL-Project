import pandas, time, pprint
import privacy
from pseudonymization import Heuristic, Hashing, Swapping

def toList(np):
    return [i[0] for i in np]

def dataDivision(currentColumnNameList:list, scopeStart=0, scopeEnd=0):
    if scopeStart & scopeEnd:
        return pandas.DataFrame.to_numpy(excel.loc[scopeStart:scopeEnd, currentColumnNameList])
    
    return pandas.DataFrame.to_numpy(excel.loc[ : , currentColumnNameList])


if __name__ == '__main__':
    start = time.time()

    # excel = pandas.read_excel('./TestExcelFiles/500000_test.xlsx', index_col=0)
    excel = pandas.read_excel('./TestExcelFiles/test.xlsx', index_col=0)
    datas = pandas.DataFrame.to_numpy(excel)

    # 컬럼명 추출
    columnList = list(excel)
    privacyIdentifier = privacy.check(columnList)
    print("개인정보 식별자 >>> ", ', '.join(privacyIdentifier))
    print()

    # names = toList(dataDivision(['이름']))
    # 휴리스틱 가명화
    # print('원본 데이터 5개만 출력 >>>', names[:5])
    
    # heuristicChangeList = [('고경화', '홍길동'), ('김성하', '임꺽정')]
    # heuristicList, heuristicFailList = Heuristic(names).change(heuristicChangeList)
    # print('휴리스틱 가명화 5개만 출력 >>> ', heuristicList[:5])
    # print('휴리스틱 가명화 실패한 대상 >>>', heuristicFailList)
    # print()
    
    # 암호화
    # print('원본 데이터 5개만 출력 >>>', names[:5])

    # hashResult, saltList = Hashing(names).sha256(randomSalt=True)
    # pprint.pprint(hashResult[:5])
    # print()

    # 교환 방식
    phone = toList(dataDivision(['전화번호']))
    print('원본 데이터 5개만 출력 >>>', phone[:5])
    
    swapList = [('010-5679-1876', '010-6457-3040'), ('010-0029-8142', '010-4174-6291')]
    swapResult = Swapping(swapList).change(phone)
    print('교환 데이터 5개만 출력 >>>', swapResult[:5])


    print(f'\n실행 시간 : {int(time.time() - start)}s')
