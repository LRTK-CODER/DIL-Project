class Swapping:
    def __init__(self, changeList):
        self.changeList = changeList
    
    def change(self, current):
        changeIndexList = [(current.index(i[0]), current.index(i[1])) for i in self.changeList]
        
        for i in changeIndexList:
            current[i[0]], current[i[1]] = current[i[1]], current[i[0]]
        
        return current
            
        