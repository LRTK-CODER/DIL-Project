import pandas, time, pprint
import privacy
from Aggregation import Aggregation, Rounding, Rearrange

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

    ages = toList(dataDivision(['나이']))
    print(f'최소/최대 나이 >>> {min(ages)}, {max(ages)}')
    print('원본 데이터 5개만 출력 >>>', ages[:5])

    # 총계처리
    aggregation = Aggregation(ages)
    print('나이 총합 >>>', aggregation.total())
    print(f'나이 평균 >>> {aggregation.average()}')

    # 부분총계
    print()
    ages[0] = 99
    print('원본 데이터 5개만 출력 >>>', ages[:5])
    aggregation = Aggregation(ages)
    ages = aggregation.micro()
    print('부분총계 결과 >>>', ages[:5])

    # 라운딩
    print()
    standard = [i*10 for i in range(1, 9)]
    rounding = Rounding(ages)
    ages = rounding.run(standard)
    print('라운딩 결과 >>>', ages[:5])

    # 재배열
    print()
    datas = pandas.DataFrame.to_numpy(excel.loc[:, columnList])
    rearrange = Rearrange(datas)
    print(datas[:10])
    print()
    print(rearrange.run([(0, 2), (5, 7)])[:10])



    print(f'\n실행 시간 : {int(time.time() - start)}s')