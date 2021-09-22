import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import statistics

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

microAggregation = statistics.MicroAggregation(excel)

# 평균값
# microAggregation.mean(column='나이', currentIndex=0)

# 최댓값
# microAggregation.max(column='나이', currentIndex=0)

# 최솟값
# microAggregation.min(column='나이', currentIndex=0)

# 최빈값
microAggregation.mode(column='나이', currentIndex=0)

print(excel.head())