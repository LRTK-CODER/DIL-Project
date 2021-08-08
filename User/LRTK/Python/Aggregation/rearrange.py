import copy

class Rearrange:
    def __init__(self, datas):
        self.datas = datas

    def run(self, changeList:list):
        current = copy.deepcopy(self.datas)
        for i, j in changeList:
            temp = current[i]
            self.datas[i] = self.datas[j]
            self.datas[j] = temp

        # for i, j in changeList:
        #     self.datas[i], self.datas[j] = self.datas[j], self.datas[i]
        
        return self.datas
