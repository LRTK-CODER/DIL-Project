class Rearrange:
    def __init__(self, datas):
        self.datas = datas

    def run(self, changeList:list):
        for i in changeList:
            self.datas[i[0]], self.datas[i[1]] = self.datas[i[1]], self.datas[i[0]]
            
        return self.datas