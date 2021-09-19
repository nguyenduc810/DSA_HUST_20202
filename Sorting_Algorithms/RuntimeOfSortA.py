"""
Thuật toán bubble sort
"""
import random as rd
import time
import  copy
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(4002)
def bubbleSort(key):
    n = len(key)
    for i in range(n -1 ):
        for j in range(0,n-i- 1):
            if key[j] > key[j+1]:
                key[j] , key[j+1] = key[j+1], key[j]
"""
Thuật toán selection sort
"""
def SelectionSort(key):
    n = len(key)
    for i in range(n-1):
        k = i
        for j in range(i+1 ,n):
            if(key[k] > key[j]):
                k = j
        if (k!= i):
            key[i], key[k] = key[k] , key[i]
"""
Thuật toán insert Sort
"""
def InsertSort(key):
    n = len(key)
    for i in range(1,n):
        vt = i -1
        x = key[i]
        while(vt>=0 and key[vt] > x):
            key[vt +1] = key[vt]
            vt -= 1
        key[vt+1] = x
"""
Thuat toan merge sort
"""

def Merge(key, left, mid, right):
    i = left
    j = mid +1
    key1 = list()
    while (i <= mid and j <= right):
        if (key[i] > key[j]):
            key1.append(key[j])
            j += 1
        else:
            key1.append(key[i])
            i += 1
    if (i > mid):
        for a in range(j, right +1):
            key1.append(key[a])
    else:
        for a in range(i,mid+1):
            key1.append(key[a])
    key[left:right+1] = key1


def MergeSort(key, left, right):
    if left < right:
        mid = int((left + right) / 2)
        MergeSort(key, left, mid)
        MergeSort(key, mid + 1, right)
        Merge(key, left, mid, right)
"""
Thuat toan heap sort 
"""
def heapify(key, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1
    if left < n and key[left] > key[largest]:
        largest = left
    if right < n and key[right] > key[largest]:
        largest = right
    if largest is not i:
        key[i], key[largest] = key[largest], key[i]
        heapify(key, n, largest)


def heapSort(key, n):
    i = int(n / 2 - 1)
    while i >= 0:
        heapify(key, n, i)
        i = i - 1
    j = n - 1
    while j > 0:
        key[j], key[0] = key[0], key[j]
        heapify(key, j, 0)
        j = j - 1
"""
thuat toan quick sort
"""
def partition(key, left , right):
    j = rd.randint(left, right)
    key[j], key[right] = key[right], key[j]
    pos = left
    pivot = key[right]
    for i in range(left ,right) :
        if key[i] <= pivot:
            key[i] , key [pos] = key[pos], key[i]
            pos +=1
    key[pos], key[right] = key[right] , key[pos]
    return pos

def quickSort(key , left ,right) :
    if left < right :
        pos = partition(key , left , right)
        quickSort(key , left , pos -1)
        quickSort(key , pos+1 , right)
"""
Ham ve do thi
"""
print(sys.getrecursionlimit())
def graphic():
    nPoints = 15
    timesBubble = list()
    timesSelection = list()
    timesInsert = list()
    timesMerge = list()
    timesQuick = list()
    n = 5000
    listPoints = list()
    key = list()
    for i in range(nPoints):
        key = list(range(n))
        #key = rd.sample(range(n), n)
        key1 = copy.copy(key)
        key2 = copy.copy(key)
        key3 = copy.copy(key)
        key4 = copy.copy(key)
        key5 = copy.copy(key)
        start = time.time()
        bubbleSort(key1)
        end = time.time()
        timesBubble.append(end - start)
        start = time.time()
        SelectionSort(key2)
        end = time.time()
        timesSelection.append(end - start)
        start = time.time()
        InsertSort(key3)
        end = time.time()
        timesInsert.append(end - start)
        start = time.time()
        MergeSort(key4, 0, len(key4) -1 )
        end = time.time()
        timesMerge.append(end - start)
        start = time.time()
        quickSort(key5,0, len(key5) -1)
        end = time.time()
        timesQuick.append(end - start)
        listPoints.append(n)
        n = n + 100
    plt.figure(figsize= (10,10))
    plt.plot(listPoints, timesBubble, 'go-', label='Bubble Sort')
    plt.plot(listPoints, timesSelection, 'ro-', label='Selection Sort')
    plt.plot(listPoints, timesInsert, 'bD-', label='Insert Sort')
    plt.plot(listPoints, timesMerge, 'g^-', label='Merge Sort')
    #plt.plot(listPoints, timesHeap, 'ro-', label='Heap Sort')
    plt.plot(listPoints, timesQuick, '-', label='Quick Sort')
    plt.legend(loc = 'best')
    plt.title('Investigate the runtime of sorting algorithms')
    plt.xlabel('The size of data')
    plt.ylabel('Running time (s)')
    plt.show()
graphic()