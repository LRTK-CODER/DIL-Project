import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import randomization

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

noiseTest = randomization.Noise(excel)

# 컬럼 1개 잡음 추가
# noiseTest.add('나이')

# 관련된 컬럼 잡음 추가
noiseTest.multipleAdd(['회원번호', '나이'])

print(excel.head())