import pandas as pd

df = pd.read_excel('./sseongmini/test.xlsx')

# 전체 통계정보? -> 집단현상에 대한 구체적인 양적 기술을 반영하는 숫자

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
generation = ['10대 미만', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대']
df['나이'] = pd.cut(df['나이'].values, bins, labels = generation, include_lowest = True)

print(df['나이'])