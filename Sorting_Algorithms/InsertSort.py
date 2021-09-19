"""
Thuật toán insert Sort
"""
import  random as rd
import time
import matplotlib
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
Tets
"""
sample = rd.sample(range(10000),10000)
print("Before: ", sample)
start = time.time()
InsertSort(sample)
end = time.time()
print("After: ", sample)
print('Thời gian chạy là : ' , end - start)