import pandas
import string
import random

dataFrame = pandas.core.frame.DataFrame

# 의사난수
# https://www.delftstack.com/ko/howto/python/random-string-python/

class prng:
    def prng(dF:dataFrame, indexSize, columns):
        number_of_strings = indexSize # 개수
        length_of_string = 0 # 길이

        for i in range(number_of_strings):
            length_of_string = len(str(dF.loc[i, columns]))
            dF.loc[i, columns] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

        return True