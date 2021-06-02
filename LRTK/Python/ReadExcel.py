import pandas, time
import privacy
from pseudonymization import Heuristic, Hashing

def toList(np):
    return [i[0] for i in np]

def dataDivision(currentColumnNameList:list, scopeStart=0, scopeEnd=0):
    if scopeStart & scopeEnd:
        return pandas.DataFrame.to_numpy(excel.loc[scopeStart:scopeEnd, currentColumnNameList])
    
    return pandas.DataFrame.to_numpy(excel.loc[ : , currentColumnNameList])


if __name__ == '__main__':
    start = time.time()

    excel = pandas.read_excel('./TestExcelFiles/500000_test.xlsx', index_col=0)
    datas = pandas.DataFrame.to_numpy(excel)

    # 컬럼명 추출
    columnList = list(excel)
    privacyIdentifier = privacy.check(columnList)
    print("개인정보 식별자 >>> ", ', '.join(privacyIdentifier))
    print()

    # 휴리스틱 가명화
    names = toList(dataDivision(['이름']))
    print('원본 데이터 5개만 출력 >>>', names[:5])
    
    heuristicChangeList = [('고경화', '홍길동'), ('김성하', '임꺽정')]
    heuristicList, heuristicFailList = Heuristic(names).change(heuristicChangeList)
    print('휴리스틱 가명화 5개만 출력 >>> ', heuristicList[:5])
    print('휴리스틱 가명화 실패한 대상 >>>', heuristicFailList)
    print()
    
    # 암호화
    

    print(f'\n실행 시간 : {int(time.time() - start)}s')