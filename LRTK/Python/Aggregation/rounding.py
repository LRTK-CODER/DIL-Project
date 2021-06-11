class Rounding:
    def __init__(self, datas:list):
        self.datas = datas

    def run(self, standard):
        for standardIdx in range(len(standard)):
            for dataIdx in range(len(self.datas)):
                if standard[standardIdx] == standard[-1]:
                    if standard[standardIdx] <= self.datas[dataIdx]:
                        self.datas[dataIdx] = standard[standardIdx]
                else:
                    if standard[standardIdx] <= self.datas[dataIdx] < standard[standardIdx+1]:
                        self.datas[dataIdx] = standard[standardIdx]

        return self.datas