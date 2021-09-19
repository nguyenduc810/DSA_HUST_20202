"""
Thuat toan merger sort
"""

import random as rd
import copy
import time
def Merger(key, left, mid, right):
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


def MergerSort(key, left, right):
    if left < right:
        mid = int((left + right) / 2)
        MergerSort(key, left, mid)
        MergerSort(key, mid + 1, right)
        Merger(key, left, mid, right)
"""
test
"""

#sample = [9,8,7,6,5,4,3,2,1]
sample = rd.sample(range(10000),10000)
print("Before: ", sample)
start = time.time()
MergerSort(sample, 0, len(sample)-1)
end = time.time()
print("After: ", sample)
print('Thời gian chạy là : ' , end - start)