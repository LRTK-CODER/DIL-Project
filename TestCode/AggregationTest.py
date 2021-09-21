import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import statistics

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

aggregation = statistics.Aggregation(excel)

# 평균값
# aggregation.mean('나이')

# 최댓값
# aggregation.max('나이')

# 최솟값
# aggregation.min('나이')

# 최빈값
# aggregation.mode('나이')

# 중간값
aggregation.median('나이')

print(excel.head())