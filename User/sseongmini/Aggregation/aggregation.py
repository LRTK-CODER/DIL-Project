import pandas as pd
import numpy as np

df = pd.read_excel('./sseongmini/test.xlsx')

# 적용정보 : 나이, 신장, 소득, 카드사용액, 유동인구, 사용자수, 제품재고량, 판매량 등

# 데이터를 부분적으로(여자, 남자) 나눈 뒤 평균을 계산하여 대체함

df['나이'] = df.groupby(['성별']).transform(np.mean)['나이']

print(df)