import array as arr
class binaryheap:
    def __init__(self):
        self.heap = list()
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def upHeapify(self, index):
        if index != 0 and index % 2 == 0:
            parent = int((index - 2) /2)
        else:
            parent = int((index -1 ) /2)
        if index != 0 and self.heap[index] < self.heap[parent]:
            self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
            self.upHeapify(parent)
    def insertHeap(self,value):
        self.heap.append(value)
        self.size += 1
        if self.size != 1:
            self.upHeapify(self.size - 1)
    def downHeapify(self, index):
        langest = index
        leftIndex = index + index +1
        rightIndex = index + index +2
        if leftIndex <= self.size -1 and self.heap[langest] > self.heap[leftIndex]:
            langest  = leftIndex
        if rightIndex <= self.size- 1 and self.heap[langest] > self.heap[rightIndex]:
            langest = rightIndex
        if langest != index :
            self.heap[langest] , self.heap[index] = self.heap[index] , self.heap[langest]
            self.downHeapify(langest)

    def removeMin(self):
        value = self.heap[0]
        self.heap[0] = self.heap[self.size -1]
        self.heap.pop(self.size -1)
        self.size -= 1
        self.downHeapify(0)
        return value

a = binaryheap()
a.insertHeap(3)
a.insertHeap(5)
a.insertHeap(6)
a.insertHeap(2)
a.insertHeap(4)
a.insertHeap(1)
print(a.heap)
a.removeMin()
a.removeMin()
a.insertHeap(10)
a.insertHeap(1)
print('After: ')
print(a.heap)


