import pandas
import string
import random

dataFrame = pandas.core.frame.DataFrame

class PRNG:
    def prng(dF:dataFrame, indexSize, columns):

        '''
        Title : (의사) 난수생성기 (Pseudo) Random Number Generator
        Creator : 홍성민
        Version : 1.0.0
        Support Type : str 

        [Explanation]
            column의 모든 값들을 의사난수화 한다.
            참고 : https://www.delftstack.com/ko/howto/python/random-string-python/

        [Parameter]
            <No Additions>
        '''
        
        number_of_strings = indexSize # 개수
        length_of_string = 0 # 길이

        for i in range(number_of_strings):
            length_of_string = len(str(dF.loc[i, columns]))
            dF.loc[i, columns] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

        return True