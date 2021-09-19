#author Nguyen Duc
import numpy as np

class graphs:
    def __init__(self,size = 0, edge = None):
        self.edge = edge
        self.size = size
        self.trace = self.size * [None]
    def dijkstra(self,start = None, end = None):
        free = self.size * [None]
        d = self.size*[None]
        self.trace[start] = -1
        free[start] = 1
        d[start] = 0
        for v in range(self.size):
            if self.edge[start][v] != 0 :
                d[v] = self.edge[start][v]
            self.trace[v] = start
        while True:
            min = 100000
            u = 0
            for v in range(self.size):
                if free[v] is None:
                    if min > d[v]:
                        min = d[v]
                        u = v
            if u == 0 or u == end:
                break
            free[u] = 1
            for v in range(self.size):
                if free[v] is None:
                    if d[v] > d[u] + self.edge[u][v]:
                        d[v] = d[u] + self.edge[u][v]
                        self.trace[v] = u
        return d[end]

    def printResult(self,start,  end):
        print('Shorts path: ',end, end = ', ')
        while end !=  start  :
            print(self.trace[end],end = ', ')
            end = self.trace[end]
def readMatrix(path):
    file = open(path, 'r')
    lt = list([int(number) for number in line.split()] for line in file)
    A = np.array(lt)
    return A

edge = readMatrix('E:\\testBFS.txt')
"""
Ma trận:
0 8 8 8 8 2
8 0 2 7 6 2
8 4 0 3 2 3
8 4 0 0 1 4
8 2 2 3 0 8
8 3 2 1 4 0
"""
g = graphs(6,edge)
d = g.dijkstra(1,4)
g.printResult(1,4)
print('\nMin path= ', d)

