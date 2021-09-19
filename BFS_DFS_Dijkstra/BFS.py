from TheQueue import *
import numpy as np
class graph:
    def __init__(self, vertices = None, edge = None):
        self.vertices = vertices
        self.edge = edge.copy()
        self.trace = len(self.vertices) * [None]
        self.check = len(self.vertices) * [None]
    def BFS(self):
        queue = Queue()
        queue.enqueue(0)
        self.check[0] = 1
        self.trace[0] = -1
        while not queue.isEmpty() :
            u = queue.dequeue()
            for i in range(len(self.vertices)):
                if self.check[i] is None and self.edge[u][i] != 0 :
                    self.check[i] = 1
                    self.trace[i] = u
                    queue.enqueue(i)
        for i in range(len(self.check)):
            if self.check[i] is None:
                print("Do thi khong lien thong!")
                return
        print('Do thi lien thong')
    def DFS(self, u):
        for v in range(len(self.vertices)):
            if self.check[v] is None and self.edge[u][v] != 0 :
                self.trace[v] = u
                self.check[v] = 1
                self.DFS(v)

def readMatrix(path):
    file = open(path, 'r')
    lt = list([int(number) for number in line.split()] for line in file)
    A = np.array(lt)
    return A

vertices = [1,2,3,4,5,6]
edge = readMatrix('E:\\testBFS.txt')
g = graph(vertices , edge)
g.trace[0] = -1
g.check[0] = 1
#g.BFS()
g.DFS(0)
c = 0
for i in range(len(g.check)):
    if g.check[i] is None:
        print('Do thi khong lien thong')
        count = 1
        break
if c == 0 :
    print('Do thi lien thong')


