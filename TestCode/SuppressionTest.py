import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import Suppression

excel = pandas.read_csv('../Sample/test_100.csv', index_col=0)
print(excel.head())

suppressionTest = Suppression(excel)

# 일반 삭제
# suppressionTest.general(['전화번호', '주소'])

# 부분 삭제
# suppressionTest.partial('이름', [1, 2])

# 레코드 삭제
# suppressionTest.record([0])
# suppressionTest.record([0, 2])

# 로컬 삭제
# suppressionTest.local('이름', [0])
# suppressionTest.local('이름', [0, 2])

# 마스킹
# suppressionTest.masking('이름', [1, 3])

# 주소 부분 삭제
# suppressionTest.address('주소', 1)
suppressionTest.address('주소', 2)

print(excel.head())