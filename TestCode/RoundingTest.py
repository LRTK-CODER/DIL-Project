import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import Rounding

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

# 반올림
# excel['나이'] = [Rounding.off(data, 1) for data in list(excel['나이'])]

# 올림
# excel['나이'] = [Rounding.up(data, 1) for data in list(excel['나이'])]

# 내림
# excel['나이'] = [Rounding.down(data, 1) for data in list(excel['나이'])]

# 랜덤 라운딩
Rounding.random(excel, '나이')

print(excel.head())