import pandas

class Heuristic:
    def __init__(self, data):
        self.data = data

    def change(self, changeList:list):
        for idx in range(len(self.data)):
            for current in changeList:
                if current[0] == self.data[idx]:
                    self.data[idx] = current[1]
                    changeList.remove(current)

        return self.data, changeList