import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import random
from util import DataSetting

class Permutation(DataSetting):
    def all(self, column:str):
        datas = self._toList(column)
        random.shuffle(datas)
        
        self.datas[column] = datas
        return self.datas[column]
