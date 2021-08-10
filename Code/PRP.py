import pandas
import string
import random

dataFrame = pandas.core.frame.DataFrame

# 의사난수
# https://www.delftstack.com/ko/howto/python/random-string-python/
def prng(dF:dataFrame, indexSize, columns):
    number_of_strings = indexSize # 개수
    length_of_string = 0 # 길이

    for i in range(number_of_strings):
        length_of_string = len(str(dF.loc[i, columns]))
        dF.loc[i, columns] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

    return True


if __name__ == '__main__':
    dataFrame = pandas.read_excel('D:/python_code/sseongmini/test.xlsx', index_col=0)
    columns = list(dataFrame.columns)
    indexSize = dataFrame.shape[0]

    prng(dataFrame, indexSize, '회원번호')
    print(dataFrame)