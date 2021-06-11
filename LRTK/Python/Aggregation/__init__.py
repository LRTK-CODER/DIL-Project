from .rounding import Rounding

__all__ = ['Rounding']

class Aggregation:
    def __init__(self, datas:list):
        self.datas = datas

    def total(self):
        return sum(self.datas)
    
    def average(self, sumValue=False):
        if sumValue is False:
            sumValue = self.total()
        return round(sumValue/len(self.datas))

    def micro(self):
        avg = self.average()
        absList = [abs(i-avg) for i in self.datas]
        self.datas[absList.index(max(absList))] = avg

        return self.datas