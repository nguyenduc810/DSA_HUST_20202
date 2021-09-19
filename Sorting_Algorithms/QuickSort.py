"""
Thuật toán quick sort (sắp xếp nhanh)
"""
import matplotlib.pyplot as plt
import random as rd
import time
import copy
from sys import setrecursionlimit
import sys

"""
def partition(key , left, right):
    pivot = key[right]
    l = left
    r = right -1
    while True:
        while l <= r and key[l] < pivot :
            l = l + 1
        while r >= l and key[r] > pivot:
            r = r -1
        if l >= r :
            break
        key[l] , key[r] = key[r] , key[l]
        l = l+1
        r = r-1
    key[l] , key[right] = key[right] , key[l]
    return l
def quickSort(key , left , right):
    if left < right:
        mid = partition(key , left , right)
        quickSort(key , left , mid-1)
        quickSort(key , mid+1 , right)

"""
"""
Test
#sample = rd.sample(range(10000), 10000)
sample = list(range(1000))
print('Before: ', sample)
print(sys.getrecursionlimit())
sys.setrecursionlimit(1002)
print(sys.getrecursionlimit())
# thời gian bắt đầu thuật toán
start = time.time()
quickSort(sample, 0, len(sample)-1)
# thời gian kết thúc thuật toán
end = time.time()
print('After: ', sample)
print('Running time: ', end - start, ' (s)')

"""
def partition(key, left , right):
    j = rd.randint(left , right)
    key[j] , key[right] = key[right] , key[j]
    pos = left
    pivot = key[right]
    for i in range(left , right):
        if key[i] <= pivot:
            key[i] , key [pos] = key[pos], key[i]
            pos +=1
    key[pos], key[right] = key[right] , key[pos]
    return pos
def partition_2(key, left , right):
    pos = left
    pivot = key[right]
    for i in range(left , right):
        if key[i] <= pivot:
            key[i] , key [pos] = key[pos], key[i]
            pos +=1
    key[pos], key[right] = key[right] , key[pos]
    return pos
def quickSort(key , left ,right) :
    if left < right :
        pos = partition(key , left , right)
        quickSort(key , left , pos-1)
        quickSort(key , pos+1 , right)
def quickSort_2(key , left ,right) :
    if left < right :
        pos = partition_2(key , left , right)
        quickSort(key , left , pos-1)
        quickSort(key , pos+1 , right)
"""
#sample = [5,8,5,7,10,6,1,4,5,3,5,5]
#quickSort(sample , 0 , len(sample) -1)
#print(sample)

#sample = rd.sample(range(10000), 10000)
"""
sys.setrecursionlimit(3000)
def graphic():
    time1 = list()
    time2 = list()
    time3 = list()
    nPoints = 10
    n = 10000
    key3 = list()
    listPoints = list()
    for i in range(nPoints):
        key1 = rd.sample(range(n), n)
        key2 = copy.copy(key1)
        for j in range(n):
            key3.append(n-1-j)
        start = time.time()
        quickSort(key1, 0, n - 1)
        end = time.time()
        time1.append(end - start)
        start = time.time()
        quickSort_2(key2, 0, n - 1)
        end = time.time()
        time2.append(end - start)
        start = time.time()
        quickSort(key3, 0, n - 1)
        end = time.time()
        time3.append(end - start)
        listPoints.append(n)
        n = n + 500
    plt.figure(figsize=(10, 10))
    plt.plot(listPoints, time1, 'go-')
    plt.plot(listPoints, time2, 'ro-')
    plt.plot(listPoints, time3, '-')
    plt.legend(loc='best')
    plt.xlabel('Data set size')
    plt.ylabel('Running time (s)')
    plt.show()
graphic()