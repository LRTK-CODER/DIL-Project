import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import randomization

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

permutationTest = randomization.Permutation(excel)

# 전체 순열
permutationTest.all('나이')

print(excel.head())