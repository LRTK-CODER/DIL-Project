import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import Generalization

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

genTest = Generalization(excel)

# 로컬 일반화
# genTest.local(column='성별', currentIndexList=[0, 3])

# 문자데이터 범주화
genTest.categorizion(column='성별', replaceList=['남성', '여성'], category='Gender')

print(excel.head())