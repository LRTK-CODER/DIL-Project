import pandas as pd
import pandas as pd

df = pd.read_excel('./sseongmini/test.xlsx')

# frac = 1 -> 100% row 데이터를 return
# reset_index를 해서 기존의 index가 아닌 새로운 indexing을 가능

df_1 = df['회원번호'].sample(frac=1).reset_index(drop=True)
df_2 = df['이름'].sample(frac=1).reset_index(drop=True)
df_3 = df['성별'].sample(frac=1).reset_index(drop=True)
df_4 = df['나이'].sample(frac=1).reset_index(drop=True)
df_5 = df['생일'].sample(frac=1).reset_index(drop=True)
df_6 = df['전화번호'].sample(frac=1).reset_index(drop=True)

df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6], axis=1)

print(df)