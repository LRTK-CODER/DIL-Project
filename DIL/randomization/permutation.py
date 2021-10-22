import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import random, numpy as np, pandas
from util import DataSetting


class Permutation(DataSetting):
    def all(self, column: str):
        datas = self.datas.loc[:, [column]]
        shuttleDatas = datas.sample(frac=1).reset_index(drop=True)

        self.datas[column] = shuttleDatas
        return self.datas[column]
