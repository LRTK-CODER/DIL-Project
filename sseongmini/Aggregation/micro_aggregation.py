import pandas as pd
import numpy as np
import scipy.stats

data = {
    'age' : [24, 36, 47],
    'height' : [176, 182, 168],
    'income' : [200, 350, 400]
}

indexName = ['홍길동', '이영희', '임꺽정']

df = pd.DataFrame(data, index=indexName)

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h


x = mean_confidence_interval(df['age'], confidence=0.95)
y = mean_confidence_interval(df['height'], confidence=0.95)
z = mean_confidence_interval(df['income'], confidence=0.95)

print(x)
print(y)
print(z)