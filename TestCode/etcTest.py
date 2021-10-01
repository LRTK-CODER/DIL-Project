import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import Etc

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

etcTest = Etc(excel)

# 샘플링
# sample = etcTest.sampling(10)
# print(sample)

identy, nonIdenty = etcTest.anatomization(identyColumn='회원번호', currentColumnList=['이름', '성별', '주소'])
print(identy.head())
print(nonIdenty.head())